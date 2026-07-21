from pathlib import Path

from python import (
    OUTCARParser,
    EIGENVALParser,
    PROCARParser,
    BandStructure,
    ElectronicStructureReport,
)

DATA = Path(__file__).parent / "data" / "gaas"


def test_report():

    outcar = OUTCARParser().read(DATA/"OUTCAR").parse()
    eigen = EIGENVALParser().read(DATA/"EIGENVAL").parse()
    procar = PROCARParser().read(DATA/"PROCAR").parse()

    bs = BandStructure.from_vasp(outcar, eigen, procar)

    report = ElectronicStructureReport(bs).as_dict()

    assert "band_gap" in report
    assert "gap_type" in report
    assert "fermi_level" in report
