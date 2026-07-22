from dataclasses import dataclass

import numpy as np


@dataclass
class BandStructure:

    efermi: float
    kpoints: np.ndarray
    weights: np.ndarray
    eigenvalues: np.ndarray
    occupations: np.ndarray
    projections: np.ndarray | None = None

    @property
    def nkpts(self):
        return self.kpoints.shape[0]

    @property
    def nbands(self):
        return self.eigenvalues.shape[1]

    @property
    def nelect(self):
        return float(self.occupations.sum() / 2.0)

    @classmethod
    def from_vasp(cls, outcar, eigenval, procar=None):

        projections = None

        if procar is not None:
            projections = procar.projections

        return cls(
            efermi=outcar.fermi,
            kpoints=eigenval.kpoints,
            weights=eigenval.weights,
            eigenvalues=eigenval.eigenvalues,
            occupations=eigenval.occupations,
            projections=projections,
        )
