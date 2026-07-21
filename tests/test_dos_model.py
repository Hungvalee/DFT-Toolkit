from pathlib import Path

from python import (
    DOS,
    DOSCARParser,
    OUTCARParser,
)

DATA = Path(__file__).parent / "data" / "gaas"


def test_dos_model():

    doscar = DOSCARParser().read(DATA/"DOSCAR").parse()

    outcar = OUTCARParser().read(DATA/"OUTCAR").parse()

    dos = DOS.from_vasp(doscar, outcar)

    assert dos.npoints == len(dos.energy)

    assert dos.efermi == outcar.fermi
