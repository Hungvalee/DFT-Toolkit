from pathlib import Path

from dft_toolkit import (
    OUTCARParser,
    EIGENVALParser,
    PROCARParser,
    BandStructure,
    BandGapAnalyzer,
)

DATA = Path(__file__).parent / "data" / "gaas"


def test_bandgap():

    outcar = OUTCARParser().read(DATA/"OUTCAR").parse()
    eigen = EIGENVALParser().read(DATA/"EIGENVAL").parse()
    procar = PROCARParser().read(DATA/"PROCAR").parse()

    bs = BandStructure.from_vasp(outcar, eigen, procar)

    analyzer = BandGapAnalyzer(bs)

    vbm = analyzer.vbm()
    cbm = analyzer.cbm()

    assert len(vbm) == 3
    assert len(cbm) == 3

    assert analyzer.band_gap() >= 0.0
