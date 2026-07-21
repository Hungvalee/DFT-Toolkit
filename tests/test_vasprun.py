from pathlib import Path

from python import VASPRUNParser

DATA = Path(__file__).parent / "data" / "vasprun"


def test_vasprun():

    data = VASPRUNParser().read(DATA/"vasprun.xml").parse()

    assert abs(data["efermi"] - 5.4321) < 1e-8
