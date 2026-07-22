"""
=========================================================
DFT Toolkit
PROCAR Parser
=========================================================
"""

import re
import numpy as np

from dft_toolkit.parsers.base import BaseParser
from dft_toolkit.core.bandstructure import BandStructure


class PROCARParser(BaseParser):

    orbital_names = [
        "s",
        "py",
        "pz",
        "px",
        "dxy",
        "dyz",
        "dz2",
        "dxz",
        "dx2",
        "tot",
    ]

    def __init__(self):

        super().__init__()

        self.nkpts = None
        self.nbands = None
        self.nions = None

        self.kpoints = []
        self.weights = []

        self.band_energy = []
        self.band_occ = []

        self.projections = None

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

        proj = []

        i = 0

        while i < len(self.lines):

            line = self.lines[i]

            #
            # k-point
            #
            if line.startswith(" k-point"):

                nums = re.findall(r"[-+]?\d+\.\d+", line)

                self.kpoints.append([
                    float(nums[0]),
                    float(nums[1]),
                    float(nums[2]),
                ])

                self.weights.append(float(nums[3]))

            #
            # band
            #
            elif line.startswith("band"):

                nums = re.findall(r"[-+]?\d+\.\d+", line)

                self.band_energy.append(float(nums[0]))
                self.band_occ.append(float(nums[1]))

                #
                # skip blank + orbital header
                #
                i += 2

                atom_proj = []

                #
                # ion table
                #
                for atom in range(self.nions):

                    cols = self.lines[i + 1 + atom].split()

                    atom_proj.append(
                        list(map(float, cols[1:11]))
                    )

                proj.append(atom_proj)

                #
                # skip
                #
                i += self.nions + 2

            i += 1

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

        self.projections = np.array(
            proj
        ).reshape(
            self.nkpts,
            self.nbands,
            self.nions,
            10
        )

        return self

    # -------------------------------------------------

    @property
    def shape(self):

        return self.band_energy.shape

    # -------------------------------------------------

    def orbital(self, atom, orbital):

        idx = self.orbital_names.index(orbital)

        return self.projections[:, :, atom - 1, idx]

    # -------------------------------------------------


    # -------------------------------------------------

    def to_bandstructure(self, efermi=0.0):

        return BandStructure(
            efermi=efermi,
            kpoints=self.kpoints,
            weights=np.ones(self.nkpts),
            eigenvalues=self.band_energy,
            occupations=self.band_occ,
            projections=self.projections,
        )


    def summary(self):

        print()

        print("=" * 60)
        print("PROCAR Summary")
        print("=" * 60)

        print(f"NKPTS : {self.nkpts}")
        print(f"NBANDS: {self.nbands}")
        print(f"NIONS : {self.nions}")

        print()

        print(f"KPOINTS    : {self.kpoints.shape}")
        print(f"BANDS      : {self.band_energy.shape}")
        print(f"OCC        : {self.band_occ.shape}")
        print(f"PROJECTION : {self.projections.shape}")

        print("=" * 60)

