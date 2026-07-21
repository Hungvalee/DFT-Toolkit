from dataclasses import dataclass
import numpy as np


@dataclass
class Structure:
    comment: str
    scale: float
    lattice: np.ndarray
    species: list
    counts: list
    frac_coords: np.ndarray

    @property
    def natoms(self):
        return sum(self.counts)

    @property
    def volume(self):
        return abs(np.linalg.det(self.lattice))
