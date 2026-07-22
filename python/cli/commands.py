from python.parsers import OUTCARParser
from python.analysis import BandGapAnalyzer


def info(filename):
    parser = OUTCARParser().read(filename)
    print(parser.parse())


def bandgap(filename):
    analyzer = BandGapAnalyzer(filename)
    print(analyzer.analyze())


def version():
    print("DFT-Toolkit v1.0.0-dev")
