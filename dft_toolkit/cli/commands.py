from dft_toolkit.parsers import OUTCARParser, EIGENVALParser
from dft_toolkit.analysis import BandGapAnalyzer


def info(filename):
    parser = OUTCARParser().read(filename).parse()
    parser.summary()


def bandgap(filename):

    parser = EIGENVALParser().read(filename).parse()

    bs = parser.to_bandstructure()

    result = BandGapAnalyzer(bs).summary()

    print()
    print("=" * 60)
    print("Band Gap")
    print("=" * 60)
    print(f"Gap : {result.gap:.6f} eV")
    print(f"VBM : {result.vbm_energy:.6f} eV")
    print(f"CBM : {result.cbm_energy:.6f} eV")
    print("=" * 60)


def version():
    print("DFT-Toolkit v1.0.0-dev")
