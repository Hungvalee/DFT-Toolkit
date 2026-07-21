from pathlib import Path

from python import KPOINTSParser

DATA = Path(__file__).parent / "data" / "kpoints"


def test_kpoints():

    kp = KPOINTSParser().read(DATA/"KPOINTS").parse()

    assert kp["mode"] == "Gamma"
    assert kp["mesh"] == [8, 8, 1]
    assert kp["shift"] == [0.0, 0.0, 0.0]
