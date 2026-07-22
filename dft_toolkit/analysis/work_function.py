import numpy as np


class WorkFunctionAnalyzer:
    """
    Analyze electrostatic potential from a LOCPOT file.

    Parameters
    ----------
    locpot : LOCPOTParser
        Parsed LOCPOT object.
    """

    def __init__(self, locpot):
        self.locpot = locpot

    def planar_average(self):
        """
        Average electrostatic potential over x-y planes.

        Returns
        -------
        numpy.ndarray
            1D potential profile along z.
        """
        return np.mean(self.locpot.potential, axis=(0, 1))

    def vacuum_level(self):
        """
        Maximum planar averaged potential.

        Returns
        -------
        float
        """
        return float(np.max(self.planar_average()))

    def work_function(self, efermi):
        """
        Calculate work function.

        Parameters
        ----------
        efermi : float
            Fermi energy from OUTCAR or vasprun.xml

        Returns
        -------
        float
        """
        return self.vacuum_level() - efermi
