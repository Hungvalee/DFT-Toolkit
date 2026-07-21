from pathlib import Path

import pytest

from python import CHGCARParser

DATA = Path(__file__).parent/"data"/"chgcar"/"CHGCAR"


def test_chgcar():

    p = CHGCARParser().read(DATA).parse()

    assert p.structure.natoms == 2

    assert p.grid == (2,2,2)

    assert p.charge.shape == (2,2,2)

    assert p.charge[0,0,0] == pytest.approx(0.10)

    assert p.charge[1,1,1] == pytest.approx(0.80)
