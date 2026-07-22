from pathlib import Path

import pytest

from dft_toolkit import EIGENVALParser

DATA = Path(__file__).parent / "data" / "gaas" / "EIGENVAL"


def test_eigenval():

    p = EIGENVALParser().read(DATA).parse()

    assert p.nelect == 8
    assert p.nkpts == 455
    assert p.nbands == 8

    assert p.eigenvalues.shape == (455, 8)
    assert p.occupations.shape == (455, 8)
    assert p.kpoints.shape == (455, 3)
    assert p.weights.shape == (455,)

    assert p.eigenvalues[0,0] == pytest.approx(-10.023773)
    assert p.eigenvalues[0,-1] == pytest.approx(6.032472)

    assert p.occupations[0,0] == pytest.approx(1.0)
    assert p.weights[0] == pytest.approx(6.4e-05)
