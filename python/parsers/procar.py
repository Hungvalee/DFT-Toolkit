"""
=========================================================
DFT Toolkit
PROCAR Parser
=========================================================
"""

import re
import numpy as np

from python.parsers.base import BaseParser


class PROCARParser(BaseParser):

    def __init__(self):

        super().__init__()

        self.nkpts = None
        self.nbands = None
        self.nions = None

        self.kpoints = []
        self.weights = []

        self.band_energy = []
        self.band_occ = []

    # -------------------------------------------------

    def parse(self):

        #
        # Header
        #
        for line in self.lines:

            if "# of k-points:" in line:

                nums = list(map(int, re.findall(r"\d+", line)))

                self.nkpts = nums[0]
                self.nbands = nums[1]
                self.nions = nums[2]

                break

        if self.nkpts is None:

            raise RuntimeError("Invalid PROCAR file.")

        #
        # Read k-points and bands
        #
        for line in self.lines:

            if line.startswith(" k-point"):

                nums = re.findall(r"[-+]?\d+\.\d+", line)

                self.kpoints.append([
                    float(nums[0]),
                    float(nums[1]),
                    float(nums[2])
                ])

                self.weights.append(float(nums[3]))

            elif line.startswith("band"):

                nums = re.findall(r"[-+]?\d+\.\d+", line)

                self.band_energy.append(float(nums[0]))
                self.band_occ.append(float(nums[1]))

        self.kpoints = np.array(self.kpoints)

        self.weights = np.array(self.weights)

        self.band_energy = np.array(
            self.band_energy
        ).reshape(
            self.nkpts,
            self.nbands
        )

        self.band_occ = np.array(
            self.band_occ
        ).reshape(
            self.nkpts,
            self.nbands
        )

        return self

    # -------------------------------------------------

    @property
    def shape(self):

        return self.band_energy.shape

    # -------------------------------------------------

    def summary(self):

        print()

        print("=" * 60)
        print("PROCAR Summary")
        print("=" * 60)

        print(f"NKPTS : {self.nkpts}")
        print(f"NBANDS: {self.nbands}")
        print(f"NIONS : {self.nions}")

        print()

        print(f"KPOINTS : {self.kpoints.shape}")
        print(f"BANDS   : {self.band_energy.shape}")
        print(f"OCC     : {self.band_occ.shape}")

        print("=" * 60)

