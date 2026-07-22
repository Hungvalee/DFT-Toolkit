from pathlib import Path

import pytest

from dft_toolkit import CHGCARParser
from dft_toolkit import ChargeDifferenceAnalyzer

DATA = Path(__file__).parent / "data" / "chgcar" / "CHGCAR"


def test_charge_difference():

    total = CHGCARParser().read(DATA).parse()
    part_a = CHGCARParser().read(DATA).parse()
    part_b = CHGCARParser().read(DATA).parse()

    cd = ChargeDifferenceAnalyzer(total, part_a, part_b)

    diff = cd.difference()

    assert diff.shape == total.charge.shape

    assert cd.max() == pytest.approx(-0.10)
    assert cd.min() == pytest.approx(-0.80)
    assert cd.mean() == pytest.approx(-0.45)
