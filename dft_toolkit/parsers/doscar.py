"""
=========================================================
DFT Toolkit
DOSCAR Parser
=========================================================
"""

import numpy as np

from dft_toolkit.parsers.base import BaseParser


class DOSCARParser(BaseParser):

    def __init__(self):

        super().__init__()

        self.nions = None
        self.nedos = None
        self.efermi = None

        self.energy = None
        self.total_dos = None
        self.integrated_dos = None

        self.blocks = []

        self.pdos = []

        self.emin = None
        self.emax = None

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

        block = []

        for line in self.lines[6:6+self.nedos]:

            cols = line.split()

            if len(cols) < 3:
                continue

            energy.append(float(cols[0]))
            dos.append(float(cols[1]))
            idos.append(float(cols[2]))

            block.append(cols)

        self.energy = np.array(energy)
        self.total_dos = np.array(dos)
        self.integrated_dos = np.array(idos)

        self.blocks.append(block)

        # -----------------------------------------------
        # Read projected DOS
        # -----------------------------------------------

        start = 6 + self.nedos

        while start < len(self.lines):

            line = self.lines[start].strip()

            if not line:
                start += 1
                continue

            start += 1

            atom = []

            for _ in range(self.nedos):

                cols = list(map(float, self.lines[start].split()))

                atom.append(cols)

                start += 1

            self.pdos.append(np.array(atom))

        self.emin = float(self.energy.min())
        self.emax = float(self.energy.max())

        return self



    @property
    def total_block(self):

        return self.blocks[0]

    # -------------------------------------------------

    @property
    def natoms(self):

        return len(self.pdos)

    # -------------------------------------------------


    # -------------------------------------------------

    @property
    def shifted_energy(self):

        return self.energy - self.efermi

    # -------------------------------------------------

    def __len__(self):

        return len(self.energy)

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
        print(f"PDOS atoms : {self.natoms}")
        print(f"Range   : {self.emin:.3f} -> {self.emax:.3f} eV")

        print("=" * 60)

