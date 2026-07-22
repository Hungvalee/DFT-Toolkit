from dataclasses import dataclass
import numpy as np


@dataclass
class DOS:
    """
    Density of States model.
    """

    energy: np.ndarray
    dos: np.ndarray
    integrated: np.ndarray | None = None
    efermi: float | None = None

    @property
    def npoints(self):
        return len(self.energy)

    @classmethod
    def from_vasp(cls, doscar, outcar=None):
        """
        Create a DOS model from parsed VASP objects.
        """
        efermi = None
        if outcar is not None:
            efermi = outcar.fermi

        return cls(
            energy=doscar.energy,
            dos=doscar.total_dos,
            integrated=doscar.integrated_dos,
            efermi=efermi,
        )

    def shifted_energy(self):
        """
        Energy referenced to the Fermi level.
        """
        if self.efermi is None:
            return self.energy

        return self.energy - self.efermi
