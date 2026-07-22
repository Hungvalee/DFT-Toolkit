from pathlib import Path

import pytest

from dft_toolkit import (
    LOCPOTParser,
    DensityProfileAnalyzer,
)

DATA = Path(__file__).parent / "data" / "locpot" / "LOCPOT"


def test_density_profile():

    locpot = LOCPOTParser().read(DATA).parse()

    dp = DensityProfileAnalyzer(locpot)

    z = dp.profile_z()

    assert len(z) == 2

    assert z[0] == pytest.approx(4.25)

    assert z[1] == pytest.approx(4.65)

    assert dp.minimum() == pytest.approx(4.25)

    assert dp.maximum() == pytest.approx(4.65)
