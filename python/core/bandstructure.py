"""
=========================================================
DFT Toolkit
Band Structure Model
=========================================================
"""

import numpy as np


class BandStructure:

    def __init__(self,
                 kpoints,
                 energies,
                 occupations=None,
                 projections=None):

        self.kpoints = np.asarray(kpoints)
        self.energies = np.asarray(energies)

        self.occupations = occupations
        self.projections = projections

    @property
    def nkpts(self):
        return self.energies.shape[0]

    @property
    def nbands(self):
        return self.energies.shape[1]

    @property
    def shape(self):
        return self.energies.shape

    def summary(self):

        print()
        print("="*60)
        print("Band Structure")
        print("="*60)
        print(f"NKPTS  : {self.nkpts}")
        print(f"NBANDS : {self.nbands}")

        print("Occupation :", self.occupations is not None)
        print("Projection :", self.projections is not None)
        print("="*60)
