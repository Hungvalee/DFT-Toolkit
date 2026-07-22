from pathlib import Path

import pytest

from dft_toolkit import CHGCARParser

DATA = Path(__file__).parent/"data"/"chgcar"/"CHGCAR"


def test_chgcar_values():

    p = CHGCARParser().read(DATA).parse()

    assert p.grid == (2,2,2)

    assert p.charge.shape == (2,2,2)

    assert p.charge.min() == pytest.approx(0.10)

    assert p.charge.max() == pytest.approx(0.80)

    assert p.charge.sum() == pytest.approx(3.60)
