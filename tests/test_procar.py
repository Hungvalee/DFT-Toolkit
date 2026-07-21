from pathlib import Path

from python import PROCARParser

DATA = Path(__file__).parent / "data" / "gaas" / "PROCAR"


def test_procar():

    p = PROCARParser().read(DATA).parse()

    assert p.nkpts == 455
    assert p.nbands == 8
    assert p.nions == 2

    assert p.band_energy.shape == (455, 8)
    assert p.band_occ.shape == (455, 8)

    assert p.projections.shape == (455, 8, 2, 10)
