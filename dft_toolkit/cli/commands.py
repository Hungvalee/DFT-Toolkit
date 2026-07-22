from dft_toolkit.parsers import OUTCARParser


def info(filename):
    parser = OUTCARParser().read(filename)
    parser.parse()
    parser.summary()


def bandgap(filename):
    print("Band gap CLI is under development.")
    print("Please use the Python API for now.")


def version():
    print("DFT-Toolkit v1.0.0-dev")
