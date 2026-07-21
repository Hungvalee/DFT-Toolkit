from pathlib import Path

from python import POTCARParser

DATA = Path(__file__).parent / "data" / "potcar"


def test_potcar():

    pot = POTCARParser().read(DATA/"POTCAR").parse()

    assert pot["elements"] == ["C", "O"]

    assert pot["enmax"] == [400.0, 500.0]

    assert pot["enmin"] == [300.0, 350.0]

    assert len(pot["potentials"]) == 2
