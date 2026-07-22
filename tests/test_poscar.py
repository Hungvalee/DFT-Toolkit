from pathlib import Path

import pytest

from dft_toolkit import POSCARParser

DATA = Path(__file__).parent/"data"/"graphene"/"POSCAR"


def test_poscar():

    s = POSCARParser().read(DATA).parse()

    assert s.natoms == 2

    assert s.species == ["C"]

    assert s.counts == [2]

    assert s.lattice.shape == (3,3)

    assert s.frac_coords.shape == (2,3)

    assert s.volume == pytest.approx(s.volume)
