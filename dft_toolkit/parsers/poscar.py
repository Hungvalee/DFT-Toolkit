import numpy as np

from .base import BaseParser
from dft_toolkit.core import Structure


class POSCARParser(BaseParser):

    def parse(self):

        comment = self.lines[0].rstrip()

        scale = float(self.lines[1])

        lattice = np.array(
            [list(map(float, self.lines[i].split()))
             for i in range(2,5)]
        ) * scale

        species = self.lines[5].split()

        counts = list(map(int,self.lines[6].split()))

        coord_type = self.lines[7].strip().lower()

        n = sum(counts)

        coords = np.array(
            [
                list(map(float,self.lines[8+i].split()[:3]))
                for i in range(n)
            ]
        )

        if coord_type.startswith("c"):
            inv = np.linalg.inv(lattice)
            coords = coords @ inv

        return Structure(
            comment,
            scale,
            lattice,
            species,
            counts,
            coords
        )
