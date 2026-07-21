from pathlib import Path

from python import (
    OUTCARParser,
    EIGENVALParser,
    PROCARParser,
    BandStructure,
)

DATA = Path(__file__).parent / "data" / "gaas"


def test_bandstructure():

    outcar = OUTCARParser().read(DATA/"OUTCAR").parse()

    eigen = EIGENVALParser().read(DATA/"EIGENVAL").parse()

    procar = PROCARParser().read(DATA/"PROCAR").parse()

    bs = BandStructure.from_vasp(
        outcar,
        eigen,
        procar,
    )

    assert bs.nkpts == 455

    assert bs.nbands == 8

    assert bs.efermi == outcar.fermi

    assert bs.projections.shape == (455,8,2,10)
