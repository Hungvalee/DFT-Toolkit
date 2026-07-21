import numpy as np

from .base import BaseParser
from python.core import Structure


class XDATCARParser(BaseParser):

    def parse(self):

        comment = self.lines[0].strip()

        scale = float(self.lines[1])

        lattice = np.array([
            list(map(float, self.lines[2].split())),
            list(map(float, self.lines[3].split())),
            list(map(float, self.lines[4].split())),
        ]) * scale

        species = self.lines[5].split()
        counts = list(map(int, self.lines[6].split()))

        natoms = sum(counts)

        structures = []

        i = 7

        while i < len(self.lines):

            line = self.lines[i].strip()

            if line.lower().startswith("direct configuration"):

                coords = np.array([
                    list(map(float, self.lines[i+1+j].split()[:3]))
                    for j in range(natoms)
                ])

                structures.append(
                    Structure(
                        comment,
                        scale,
                        lattice.copy(),
                        species.copy(),
                        counts.copy(),
                        coords
                    )
                )

                i += natoms + 1

            else:
                i += 1

        self.structures = structures

        return self
