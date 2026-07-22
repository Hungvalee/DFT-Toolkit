import numpy as np

from .base import BaseParser
from dft_toolkit.core import Structure


class CHGCARParser(BaseParser):

    def parse(self):

        comment = self.lines[0].strip()

        scale = float(self.lines[1])

        lattice = np.array([
            list(map(float, self.lines[2].split())),
            list(map(float, self.lines[3].split())),
            list(map(float, self.lines[4].split()))
        ]) * scale

        species = self.lines[5].split()
        counts = list(map(int, self.lines[6].split()))

        natoms = sum(counts)

        line = 7

        if self.lines[line].strip().lower().startswith("selective"):
            line += 1

        coord_type = self.lines[line].strip().lower()
        line += 1

        coords = np.array([
            list(map(float, self.lines[line+i].split()[:3]))
            for i in range(natoms)
        ])

        if coord_type.startswith("c"):
            coords = coords @ np.linalg.inv(lattice)

        structure = Structure(
            comment,
            scale,
            lattice,
            species,
            counts,
            coords
        )

        line += natoms

        while line < len(self.lines):

            cols = self.lines[line].split()

            if len(cols) == 3:

                try:
                    nx, ny, nz = map(int, cols)
                    break
                except ValueError:
                    pass

            line += 1

        line += 1

        values = []

        while line < len(self.lines):

            cols = self.lines[line].split()

            try:
                values.extend(map(float, cols))
            except ValueError:
                break

            line += 1

        expected = nx * ny * nz

        if len(values) < expected:
            raise ValueError(
                f"Expected {expected} grid values but got {len(values)}"
            )

        rho = np.array(values[:expected])

        rho = rho.reshape((nx, ny, nz), order="F")

        self.structure = structure
        self.grid = (nx, ny, nz)
        self.charge = rho

        return self
