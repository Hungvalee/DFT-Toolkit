from dataclasses import dataclass
import numpy as np


@dataclass
class KPath:
    """
    High-symmetry k-point path.
    """

    coordinates: np.ndarray
    labels: list[str] | None = None

    @property
    def nkpts(self):
        return len(self.coordinates)

    def distances(self):
        """
        Cumulative distance along the path.
        """

        coords = np.asarray(self.coordinates)

        d = np.zeros(len(coords))

        if len(coords) < 2:
            return d

        step = np.linalg.norm(coords[1:] - coords[:-1], axis=1)

        d[1:] = np.cumsum(step)

        return d
