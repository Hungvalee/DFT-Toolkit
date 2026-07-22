"""
=========================================================
DFT Toolkit for VASP
POSCAR I/O
=========================================================
"""

from pathlib import Path
import math


class PoscarError(Exception):
    """POSCAR related errors."""
    pass


class Poscar:
    """
    POSCAR reader/writer.
    """

    def __init__(self):

        self.comment = ""
        self.scale = 1.0

        self.lattice = []

        self.elements = []
        self.counts = []

        self.coordinate_type = "Direct"

        self.coordinates = []

        self.selective_dynamics = False
        self.flags = []

    # -----------------------------------------------------

    @property
    def natoms(self):
        return sum(self.counts)

    # -----------------------------------------------------

    @property
    def species(self):
        return list(self.elements)

    # -----------------------------------------------------

    @property
    def formula(self):

        out = []

        for e, n in zip(self.elements, self.counts):

            out.append(e)

            if n != 1:
                out.append(str(n))

        return "".join(out)

    # -----------------------------------------------------

    @property
    def is_direct(self):

        return self.coordinate_type.lower().startswith("d")

    # -----------------------------------------------------

    @property
    def is_cartesian(self):

        return self.coordinate_type.lower().startswith("c")

    # -----------------------------------------------------

    @property
    def volume(self):

        a = self.lattice[0]
        b = self.lattice[1]
        c = self.lattice[2]

        return abs(
            a[0]*(b[1]*c[2]-b[2]*c[1])
          - a[1]*(b[0]*c[2]-b[2]*c[0])
          + a[2]*(b[0]*c[1]-b[1]*c[0])
        ) * self.scale**3

    # -----------------------------------------------------

    @property
    def reciprocal_lattice(self):

        a = [x*self.scale for x in self.lattice[0]]
        b = [x*self.scale for x in self.lattice[1]]
        c = [x*self.scale for x in self.lattice[2]]

        def cross(u,v):
            return [
                u[1]*v[2]-u[2]*v[1],
                u[2]*v[0]-u[0]*v[2],
                u[0]*v[1]-u[1]*v[0],
            ]

        def dot(u,v):
            return sum(i*j for i,j in zip(u,v))

        v = dot(a,cross(b,c))

        factor = 2*math.pi/v

        b1 = [factor*x for x in cross(b,c)]
        b2 = [factor*x for x in cross(c,a)]
        b3 = [factor*x for x in cross(a,b)]

        return [b1,b2,b3]

    # -----------------------------------------------------

    def read(self, filename):

        text = Path(filename).read_text()

        return self.from_string(text)

    # -----------------------------------------------------

    def from_string(self, text):

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if len(lines) < 8:
            raise PoscarError("Invalid POSCAR.")

        i = 0

        self.comment = lines[i]
        i += 1

        self.scale = float(lines[i])
        i += 1

        self.lattice = []

        for _ in range(3):

            self.lattice.append(
                list(map(float, lines[i].split()))
            )

            i += 1

        # VASP5
        if lines[i].split()[0].isalpha():

            self.elements = lines[i].split()
            i += 1

        else:

            self.elements = []

        self.counts = list(map(int, lines[i].split()))
        i += 1

        if not self.elements:

            self.elements = [
                f"X{k+1}"
                for k in range(len(self.counts))
            ]

        if lines[i].lower().startswith("selective"):

            self.selective_dynamics = True
            i += 1

        else:

            self.selective_dynamics = False

        self.coordinate_type = lines[i]
        i += 1

        self.coordinates = []
        self.flags = []

        for _ in range(self.natoms):

            fields = lines[i].split()

            self.coordinates.append(
                list(map(float, fields[:3]))
            )

            if self.selective_dynamics:

                self.flags.append(fields[3:6])

            i += 1

        self.validate()

        return self

    # -----------------------------------------------------

    def validate(self):

        if len(self.lattice) != 3:
            raise PoscarError("Invalid lattice.")

        if len(self.counts) != len(self.elements):
            raise PoscarError("Species mismatch.")

        if len(self.coordinates) != self.natoms:
            raise PoscarError("Wrong number of atoms.")

    # -----------------------------------------------------

    def to_string(self):

        out = []

        out.append(self.comment)
        out.append(f"{self.scale:.16f}")

        for vec in self.lattice:

            out.append(
                "{:16.10f} {:16.10f} {:16.10f}".format(*vec)
            )

        out.append(" ".join(self.elements))
        out.append(
            " ".join(map(str, self.counts))
        )

        if self.selective_dynamics:

            out.append("Selective Dynamics")

        out.append(self.coordinate_type)

        for n, xyz in enumerate(self.coordinates):

            line = (
                "{:16.10f} {:16.10f} {:16.10f}"
                .format(*xyz)
            )

            if self.selective_dynamics:

                line += " " + " ".join(self.flags[n])

            out.append(line)

        return "\n".join(out) + "\n"

    # -----------------------------------------------------

    def write(self, filename):

        Path(filename).write_text(
            self.to_string()
        )

        return filename

    # -----------------------------------------------------

    # -----------------------------------------------------

    @staticmethod
    def _dot(a, b):
        return sum(x * y for x, y in zip(a, b))

    # -----------------------------------------------------

    @staticmethod
    def _matvec(m, v):
        return [
            m[0][0]*v[0] + m[0][1]*v[1] + m[0][2]*v[2],
            m[1][0]*v[0] + m[1][1]*v[1] + m[1][2]*v[2],
            m[2][0]*v[0] + m[2][1]*v[1] + m[2][2]*v[2],
        ]

    # -----------------------------------------------------

    @staticmethod
    def _inverse3(m):

        a,b,c = m[0]
        d,e,f = m[1]
        g,h,i = m[2]

        det = (
            a*(e*i-f*h)
            - b*(d*i-f*g)
            + c*(d*h-e*g)
        )

        if abs(det) < 1e-12:
            raise PoscarError("Singular lattice matrix.")

        return [
            [(e*i-f*h)/det, (c*h-b*i)/det, (b*f-c*e)/det],
            [(f*g-d*i)/det, (a*i-c*g)/det, (c*d-a*f)/det],
            [(d*h-e*g)/det, (b*g-a*h)/det, (a*e-b*d)/det],
        ]

    # -----------------------------------------------------

    def to_cartesian(self):

        if self.is_cartesian:
            return

        lattice = [
            [x*self.scale for x in row]
            for row in self.lattice
        ]

        self.coordinates = [
            self._matvec(lattice, p)
            for p in self.coordinates
        ]

        self.coordinate_type = "Cartesian"

    # -----------------------------------------------------

    def to_direct(self):

        if self.is_direct:
            return

        lattice = [
            [x*self.scale for x in row]
            for row in self.lattice
        ]

        inv = self._inverse3(lattice)

        self.coordinates = [
            self._matvec(inv, p)
            for p in self.coordinates
        ]

        self.coordinate_type = "Direct"

    # -----------------------------------------------------

    def translate(self, dx=0.0, dy=0.0, dz=0.0):

        for xyz in self.coordinates:
            xyz[0] += dx
            xyz[1] += dy
            xyz[2] += dz

    # -----------------------------------------------------

    def center(self):

        if not self.coordinates:
            return

        if self.is_cartesian:
            self.to_direct()

        xs = [c[0] for c in self.coordinates]
        ys = [c[1] for c in self.coordinates]
        zs = [c[2] for c in self.coordinates]

        self.translate(
            0.5 - (min(xs)+max(xs))/2,
            0.5 - (min(ys)+max(ys))/2,
            0.5 - (min(zs)+max(zs))/2,
        )

    # -----------------------------------------------------

    # -----------------------------------------------------

    def scale_lattice(self, factor):

        self.scale *= float(factor)

    # -----------------------------------------------------

    def add_vacuum(self, vacuum, axis="z"):

        if not self.is_cartesian:
            self.to_cartesian()

        axis = axis.lower()

        idx = {"x":0, "y":1, "z":2}[axis]

        length = (
            self.lattice[idx][0]**2 +
            self.lattice[idx][1]**2 +
            self.lattice[idx][2]**2
        )**0.5 * self.scale

        new_length = length + vacuum

        factor = new_length / length

        self.lattice[idx] = [
            x * factor
            for x in self.lattice[idx]
        ]

        self.to_direct()

    # -----------------------------------------------------

    def supercell(self, nx=1, ny=1, nz=1):

        if not self.is_direct:
            self.to_direct()

        new_coords = []

        total = nx * ny * nz

        for ix in range(nx):
            for iy in range(ny):
                for iz in range(nz):

                    shift = [ix, iy, iz]

                    for xyz in self.coordinates:

                        new_coords.append([
                            (xyz[0] + shift[0]) / nx,
                            (xyz[1] + shift[1]) / ny,
                            (xyz[2] + shift[2]) / nz,
                        ])

        self.coordinates = new_coords

        self.counts = [
            n * total
            for n in self.counts
        ]

        self.lattice[0] = [
            x * nx
            for x in self.lattice[0]
        ]

        self.lattice[1] = [
            x * ny
            for x in self.lattice[1]
        ]

        self.lattice[2] = [
            x * nz
            for x in self.lattice[2]
        ]

    # -----------------------------------------------------

    # -----------------------------------------------------

    def scale_lattice(self, factor):

        self.scale *= float(factor)

    # -----------------------------------------------------

    def add_vacuum(self, vacuum, axis="z"):

        axis = axis.lower()

        index = {"x":0, "y":1, "z":2}[axis]

        length = (
            self.lattice[index][0]**2 +
            self.lattice[index][1]**2 +
            self.lattice[index][2]**2
        )**0.5

        factor = (length*self.scale + vacuum)/(length*self.scale)

        self.lattice[index] = [
            x*factor
            for x in self.lattice[index]
        ]

    # -----------------------------------------------------

    def supercell(self, nx=1, ny=1, nz=1):

        if not self.is_direct:
            raise PoscarError(
                "supercell() requires Direct coordinates."
            )

        new_coords = []

        for ix in range(nx):
            for iy in range(ny):
                for iz in range(nz):

                    for xyz in self.coordinates:

                        new_coords.append([
                            (xyz[0]+ix)/nx,
                            (xyz[1]+iy)/ny,
                            (xyz[2]+iz)/nz,
                        ])

        self.coordinates = new_coords

        factor = nx*ny*nz

        self.counts = [
            n*factor
            for n in self.counts
        ]

        self.lattice[0] = [
            x*nx
            for x in self.lattice[0]
        ]

        self.lattice[1] = [
            x*ny
            for x in self.lattice[1]
        ]

        self.lattice[2] = [
            x*nz
            for x in self.lattice[2]
        ]

    # -----------------------------------------------------

    def summary(self):

        print("POSCAR Summary")
        print("-" * 40)

        print("Comment :", self.comment)
        print("Species :", " ".join(self.elements))
        print("Counts  :", self.counts)
        print("Atoms   :", self.natoms)
        print("Coord   :", self.coordinate_type)
