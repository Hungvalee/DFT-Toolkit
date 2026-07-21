from pathlib import Path

from python import DOSCARParser

DATA = Path(__file__).parent / "data" / "gaas" / "DOSCAR"


def test_doscar():

    p = DOSCARParser().read(DATA).parse()

    assert p.nedos == 3000
    assert p.natoms == 2
    assert p.energy.shape == (3000,)
