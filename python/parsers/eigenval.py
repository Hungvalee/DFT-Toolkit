"""
=========================================================
DFT Toolkit
EIGENVAL Parser
=========================================================
"""

import numpy as np

from python.parsers.base import BaseParser


class EIGENVALParser(BaseParser):

    def __init__(self):

        super().__init__()

        self.nelect = None
        self.nkpts = None
        self.nbands = None

        self.kpoints = None
        self.weights = None
        self.eigenvalues = None

    # -------------------------------------------------

    def parse(self):

        #
        # line 6:
        # nelect nkpts nbands
        #
        head = self.lines[5].split()

        self.nelect = int(head[0])
        self.nkpts = int(head[1])
        self.nbands = int(head[2])

        kpts = []
        weights = []
        eig = []

        i = 7

        for k in range(self.nkpts):

            #
            # kx ky kz weight
            #
            cols = self.lines[i].split()

            kpts.append([
                float(cols[0]),
                float(cols[1]),
                float(cols[2])
            ])

            weights.append(float(cols[3]))

            bands = []

            for j in range(self.nbands):

                cols = self.lines[i+1+j].split()

                bands.append(float(cols[1]))

            eig.append(bands)

            i += self.nbands + 2

        self.kpoints = np.array(kpts)

        self.weights = np.array(weights)

        self.eigenvalues = np.array(eig)

        return self


    # -------------------------------------------------

    @property
    def shape(self):

        return self.eigenvalues.shape

    # -------------------------------------------------

    @property
    def bands(self):

        return range(self.nbands)

    # -------------------------------------------------

    def __len__(self):

        return self.nkpts

    # -------------------------------------------------

    def summary(self):

        print()

        print("="*60)

        print("EIGENVAL Summary")

        print("="*60)

        print(f"NELECT : {self.nelect}")
        print(f"NKPTS  : {self.nkpts}")
        print(f"NBANDS : {self.nbands}")

        print()

        print(f"Shape   : {self.shape}")
        print(f"K-points: {len(self)}")

        print("="*60)

