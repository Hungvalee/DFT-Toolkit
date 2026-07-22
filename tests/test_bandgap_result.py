from pathlib import Path

from dft_toolkit import (
    OUTCARParser,
    EIGENVALParser,
    PROCARParser,
    BandStructure,
    BandGapAnalyzer,
)

DATA = Path(__file__).parent / "data" / "gaas"


def test_bandgap_result():

    outcar = OUTCARParser().read(DATA/"OUTCAR").parse()
    eigen = EIGENVALParser().read(DATA/"EIGENVAL").parse()
    procar = PROCARParser().read(DATA/"PROCAR").parse()

    bs = BandStructure.from_vasp(outcar, eigen, procar)

    result = BandGapAnalyzer(bs).summary()

    assert result.gap >= 0.0
    assert result.gap_type in ("direct", "indirect")
    assert isinstance(result.is_direct, bool)
