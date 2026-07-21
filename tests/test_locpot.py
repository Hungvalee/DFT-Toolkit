from pathlib import Path

import pytest

from python import LOCPOTParser

DATA = Path(__file__).parent/"data"/"locpot"/"LOCPOT"


def test_locpot():

    p = LOCPOTParser().read(DATA).parse()

    assert p.structure.natoms == 2

    assert p.grid == (2,2,2)

    assert p.potential.shape == (2,2,2)

    assert p.potential.min() == pytest.approx(4.10)
    assert p.potential.max() == pytest.approx(4.80)
    assert p.potential.mean() == pytest.approx(4.45)
