import numpy as np

from python.core import BandGapResult


class BandGapAnalyzer:
    """
    Analyze the band gap from a BandStructure object.
    """

    def __init__(self, bandstructure):
        self.bs = bandstructure

    def vbm(self):
        """
        Return the Valence Band Maximum (VBM).

        Returns
        -------
        tuple
            (energy, kpoint_index, band_index)
        """
        occ = self.bs.occupations > 0.5

        energies = np.where(
            occ,
            self.bs.eigenvalues,
            -np.inf,
        )

        idx = np.unravel_index(
            np.argmax(energies),
            energies.shape,
        )

        return (
            float(energies[idx]),
            int(idx[0]),
            int(idx[1]),
        )

    def cbm(self):
        """
        Return the Conduction Band Minimum (CBM).

        Returns
        -------
        tuple
            (energy, kpoint_index, band_index)
        """
        occ = self.bs.occupations <= 0.5

        energies = np.where(
            occ,
            self.bs.eigenvalues,
            np.inf,
        )

        idx = np.unravel_index(
            np.argmin(energies),
            energies.shape,
        )

        return (
            float(energies[idx]),
            int(idx[0]),
            int(idx[1]),
        )

    def band_gap(self):
        """
        Return the fundamental band gap.
        """
        return self.cbm()[0] - self.vbm()[0]

    def summary(self):
        """
        Return a BandGapResult object.
        """
        vbm = self.vbm()
        cbm = self.cbm()

        return BandGapResult(
            gap=cbm[0] - vbm[0],
            vbm_energy=vbm[0],
            cbm_energy=cbm[0],
            vbm_kpoint=vbm[1],
            cbm_kpoint=cbm[1],
            vbm_band=vbm[2],
            cbm_band=cbm[2],
        )
