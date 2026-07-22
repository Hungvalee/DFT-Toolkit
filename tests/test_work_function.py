from pathlib import Path

import pytest

from dft_toolkit import LOCPOTParser
from dft_toolkit import WorkFunctionAnalyzer

DATA = Path(__file__).parent / "data" / "locpot" / "LOCPOT"


def test_planar_average():

    locpot = LOCPOTParser().read(DATA).parse()

    wf = WorkFunctionAnalyzer(locpot)

    avg = wf.planar_average()

    assert len(avg) == 2


def test_vacuum_level():

    locpot = LOCPOTParser().read(DATA).parse()

    wf = WorkFunctionAnalyzer(locpot)

    assert wf.vacuum_level() == pytest.approx(4.65)


def test_work_function():

    locpot = LOCPOTParser().read(DATA).parse()

    wf = WorkFunctionAnalyzer(locpot)

    assert wf.work_function(2.30) == pytest.approx(2.35)
