from pathlib import Path

import pytest

from python import XDATCARParser

DATA = Path(__file__).parent/"data"/"xdatcar"/"XDATCAR"


def test_xdatcar():

    p = XDATCARParser().read(DATA).parse()

    assert len(p.structures) == 2

    s0 = p.structures[0]

    assert s0.natoms == 2

    assert s0.species == ["C"]

    assert s0.counts == [2]

    assert s0.frac_coords.shape == (2,3)

    assert s0.frac_coords[0,0] == pytest.approx(0.333333)

    s1 = p.structures[1]

    assert s1.frac_coords[0,0] == pytest.approx(0.334333)
