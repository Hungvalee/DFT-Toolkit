import numpy as np


class DensityProfileAnalyzer:
    """
    Compute planar-averaged profiles from 3D volumetric data.
    """

    def __init__(self, data):
        """
        Parameters
        ----------
        data : CHGCARParser or LOCPOTParser
            Parsed volumetric dataset.
        """
        if hasattr(data, "charge"):
            self.values = data.charge
        elif hasattr(data, "potential"):
            self.values = data.potential
        else:
            raise TypeError(
                "Input object must contain either 'charge' or 'potential'."
            )

    def profile_x(self):
        return np.mean(self.values, axis=(1, 2))

    def profile_y(self):
        return np.mean(self.values, axis=(0, 2))

    def profile_z(self):
        return np.mean(self.values, axis=(0, 1))

    def maximum(self):
        return float(np.max(self.profile_z()))

    def minimum(self):
        return float(np.min(self.profile_z()))
