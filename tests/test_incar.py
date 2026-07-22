from pathlib import Path

from dft_toolkit import INCARParser

DATA = Path(__file__).parent / "data" / "incar"


def test_incar():

    incar = INCARParser().read(DATA/"INCAR").parse()

    assert incar["ENCUT"] == "520"
    assert incar["ISMEAR"] == "0"
    assert incar["SIGMA"] == "0.05"
    assert incar["NSW"] == "0"
