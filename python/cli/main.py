import argparse

from python.parsers import OUTCARParser
from python.analysis import BandGapAnalyzer


def cmd_info(args):
    parser = OUTCARParser().read(args.file)
    data = parser.parse()
    print(data)


def cmd_bandgap(args):
    analyzer = BandGapAnalyzer(args.file)
    result = analyzer.analyze()
    print(result)


def main():

    parser = argparse.ArgumentParser(
        prog="dft-toolkit",
        description="DFT-Toolkit command-line interface"
    )

    subparsers = parser.add_subparsers(dest="command")

    info = subparsers.add_parser(
        "info",
        help="Read OUTCAR information"
    )
    info.add_argument("file")
    info.set_defaults(func=cmd_info)

    bandgap = subparsers.add_parser(
        "bandgap",
        help="Calculate band gap"
    )
    bandgap.add_argument("file")
    bandgap.set_defaults(func=cmd_bandgap)

    version = subparsers.add_parser(
        "version",
        help="Show version"
    )

    args = parser.parse_args()

    if args.command == "version":
        print("DFT-Toolkit v1.0.0-dev")
        return

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
