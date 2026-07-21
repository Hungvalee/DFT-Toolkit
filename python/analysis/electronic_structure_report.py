from python.analysis.bandgap import BandGapAnalyzer


class ElectronicStructureReport:
    """
    Summarize electronic structure properties.
    """

    def __init__(self, bandstructure):
        self.bs = bandstructure

    def as_dict(self):

        bg = BandGapAnalyzer(self.bs).summary()

        return {
            "band_gap": bg.gap,
            "gap_type": bg.gap_type,
            "vbm_energy": bg.vbm_energy,
            "cbm_energy": bg.cbm_energy,
            "vbm_kpoint": bg.vbm_kpoint,
            "cbm_kpoint": bg.cbm_kpoint,
            "fermi_level": self.bs.efermi,
        }
