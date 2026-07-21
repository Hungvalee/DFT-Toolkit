from pathlib import Path

from python import (
    OUTCARParser,
    EIGENVALParser,
    PROCARParser,
    BandStructure,
    BandStructureWriter,
)

DATA = Path(__file__).parent / "data" / "gaas"


def test_bandstructure_writer(tmp_path):

    outcar = OUTCARParser().read(DATA/"OUTCAR").parse()
    eigen = EIGENVALParser().read(DATA/"EIGENVAL").parse()
    procar = PROCARParser().read(DATA/"PROCAR").parse()

    bs = BandStructure.from_vasp(outcar, eigen, procar)

    outfile = tmp_path / "bands.dat"

    BandStructureWriter.write(outfile, bs)

    assert outfile.exists()

    lines = outfile.read_text().splitlines()

    assert len(lines) == bs.nkpts + 1
