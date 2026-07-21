import numpy as np


class EffectiveMassAnalyzer:
    """
    Estimate effective mass from a band structure.

    The returned value is proportional to the inverse curvature.
    Physical units require conversion using lattice vectors and
    reciprocal-space distances.
    """

    def __init__(self, bandstructure):
        self.bs = bandstructure

    def curvature(self, band, kpoint):
        """
        Finite-difference second derivative.
        """

        if kpoint == 0 or kpoint == self.bs.nkpts - 1:
            raise ValueError("Need an interior k-point")

        e = self.bs.eigenvalues[:, band]

        return e[kpoint + 1] - 2 * e[kpoint] + e[kpoint - 1]

    def effective_mass(self, band, kpoint):
        """
        Effective mass in arbitrary units.

        m* ∝ 1 / (d²E/dk²)
        """

        c = self.curvature(band, kpoint)

        if abs(c) < 1e-12:
            raise ZeroDivisionError("Zero curvature")

        return 1.0 / c
