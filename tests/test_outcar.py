from pathlib import Path

from dft_toolkit import OUTCARParser

DATA = Path(__file__).parent / "data" / "gaas" / "OUTCAR"


def test_outcar():

    p = OUTCARParser().read(DATA).parse()

    assert p.fermi is not None
    assert abs(p.fermi - 2.2877) < 1e-4
    assert p.nelect == 8.0
    assert p.nions == 2
    assert p.converged is True
