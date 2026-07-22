from pathlib import Path

import pytest

from dft_toolkit import PROCARParser

DATA = Path(__file__).parent / "data" / "gaas" / "PROCAR"


def test_procar():

    p = PROCARParser().read(DATA).parse()

    assert p.nkpts == 455
    assert p.nbands == 8
    assert p.nions == 2

    assert p.band_energy.shape == (455, 8)
    assert p.band_occ.shape == (455, 8)
    assert p.kpoints.shape == (455, 3)
    assert p.weights.shape == (455,)
    assert p.projections.shape == (455, 8, 2, 10)

    assert p.band_energy[0,0] == pytest.approx(-10.02377286)
    assert p.band_occ[0,0] == pytest.approx(2.0)
    assert p.projections[0,0,0,0] == pytest.approx(0.234)

    assert p.weights[0] == pytest.approx(6.4e-05)
