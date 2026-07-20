"""
=========================================================
DFT Toolkit
DOSCAR Parser
=========================================================
"""

import numpy as np

from python.parsers.base import BaseParser


class DOSCARParser(BaseParser):

    def __init__(self):

        super().__init__()

        self.nions = None
        self.nedos = None
        self.efermi = None

        self.energy = None
        self.total_dos = None
        self.integrated_dos = None

    # -------------------------------------------------

    def parse(self):

        if len(self.lines) < 7:
            raise ValueError("Invalid DOSCAR file.")

        #
        # Line 1:
        # NIONS ...
        #
        self.nions = int(self.lines[0].split()[0])

        #
        # Line 6:
        # Emax Emin NEDOS Efermi ...
        #
        header = self.lines[5].split()

        self.nedos = int(header[2])
        self.efermi = float(header[3])

        energy = []
        dos = []
        idos = []

        for line in self.lines[6:6+self.nedos]:

            cols = line.split()

            if len(cols) < 3:
                continue

            energy.append(float(cols[0]))
            dos.append(float(cols[1]))
            idos.append(float(cols[2]))

        self.energy = np.array(energy)
        self.total_dos = np.array(dos)
        self.integrated_dos = np.array(idos)

        return self

    # -------------------------------------------------

    def summary(self):

        print()
        print("=" * 60)
        print("DOSCAR Summary")
        print("=" * 60)

        print(f"NIONS   : {self.nions}")
        print(f"NEDOS   : {self.nedos}")
        print(f"E-fermi : {self.efermi}")
        print(f"Points  : {len(self.energy)}")

        print("=" * 60)

