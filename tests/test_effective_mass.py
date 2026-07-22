from pathlib import Path

from dft_toolkit import (
    OUTCARParser,
    EIGENVALParser,
    PROCARParser,
    BandStructure,
    EffectiveMassAnalyzer,
)

DATA = Path(__file__).parent / "data" / "gaas"


def test_effective_mass():

    outcar = OUTCARParser().read(DATA/"OUTCAR").parse()

    eigen = EIGENVALParser().read(DATA/"EIGENVAL").parse()

    procar = PROCARParser().read(DATA/"PROCAR").parse()

    bs = BandStructure.from_vasp(outcar, eigen, procar)

    em = EffectiveMassAnalyzer(bs)

    value = em.effective_mass(3, 100)

    assert isinstance(value, float)
