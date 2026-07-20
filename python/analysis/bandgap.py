"""
=========================================================
DFT Toolkit
Band Gap Analyzer
=========================================================
"""

import numpy as np


class BandGapAnalyzer:

    def __init__(self, parser):

        self.parser = parser

        self.vbm = None
        self.cbm = None
        self.gap = None

        self.vbm_kpoint = None
        self.cbm_kpoint = None

        self.vbm_band = None
        self.cbm_band = None

    # -------------------------------------------------

    def analyze(self):

        eig = self.parser.eigenvalues
        occ = self.parser.occupations

        occ_mask = occ > 0.5
        emp_mask = occ <= 0.5

        occupied = eig[occ_mask]
        empty = eig[emp_mask]

        if occupied.size == 0:
            raise RuntimeError("No occupied states found.")

        if empty.size == 0:
            raise RuntimeError("No unoccupied states found.")

        self.vbm = occupied.max()
        self.cbm = empty.min()

        self.gap = self.cbm - self.vbm

        self.vbm_kpoint, self.vbm_band = np.argwhere(
            (eig == self.vbm) & occ_mask
        )[0]

        self.cbm_kpoint, self.cbm_band = np.argwhere(
            (eig == self.cbm) & emp_mask
        )[0]

        return self

    # -------------------------------------------------

    @property
    def is_direct(self):

        return self.vbm_kpoint == self.cbm_kpoint

    # -------------------------------------------------

    @property
    def gap_type(self):

        return "Direct" if self.is_direct else "Indirect"

    # -------------------------------------------------

    def to_dict(self):

        return {

            "vbm": float(self.vbm),
            "cbm": float(self.cbm),
            "gap": float(self.gap),

            "gap_type": self.gap_type,

            "vbm_kpoint": int(self.vbm_kpoint),
            "cbm_kpoint": int(self.cbm_kpoint),

            "vbm_band": int(self.vbm_band),
            "cbm_band": int(self.cbm_band)

        }

    # -------------------------------------------------

    def summary(self):

        print()
        print("=" * 60)
        print("Band Gap Analysis")
        print("=" * 60)

        print(f"VBM : {self.vbm:.6f} eV")
        print(f"CBM : {self.cbm:.6f} eV")
        print(f"Gap : {self.gap:.6f} eV")

        print()

        print(f"VBM k-point : {self.vbm_kpoint}")
        print(f"VBM band    : {self.vbm_band}")

        print(f"CBM k-point : {self.cbm_kpoint}")
        print(f"CBM band    : {self.cbm_band}")

        print()

        print(f"Gap type    : {self.gap_type}")

        print("=" * 60)

