from dataclasses import dataclass


@dataclass(frozen=True)
class BandGapResult:
    """
    Result of a band gap analysis.
    """

    gap: float

    vbm_energy: float
    cbm_energy: float

    vbm_kpoint: int
    cbm_kpoint: int

    vbm_band: int
    cbm_band: int

    @property
    def is_direct(self):
        return self.vbm_kpoint == self.cbm_kpoint

    @property
    def gap_type(self):
        return "direct" if self.is_direct else "indirect"
