from pathlib import Path

from python import EIGENVALParser

DATA = Path(__file__).parent / "data" / "gaas" / "EIGENVAL"


def test_eigenval():

    p = EIGENVALParser().read(DATA).parse()

    assert p.nkpts == 455
    assert p.nbands == 8

    assert p.eigenvalues.shape == (455, 8)
    assert p.occupations.shape == (455, 8)
