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

    def summary(self):

        print("POSCAR Summary")
        print("-" * 40)

        print("Comment :", self.comment)
        print("Species :", " ".join(self.elements))
        print("Counts  :", self.counts)
        print("Atoms   :", self.natoms)
        print("Coord   :", self.coordinate_type)
