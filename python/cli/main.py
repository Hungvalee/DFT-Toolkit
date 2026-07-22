import argparse

from . import commands


def main():
    parser = argparse.ArgumentParser(
        prog="dft-toolkit",
        description="DFT-Toolkit command-line interface"
    )

    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("info", help="Read OUTCAR information")
    p.add_argument("file")

    p = sub.add_parser("bandgap", help="Calculate band gap")
    p.add_argument("file")

    sub.add_parser("version", help="Show version")

    args = parser.parse_args()

    if args.command == "info":
        commands.info(args.file)

    elif args.command == "bandgap":
        commands.bandgap(args.file)

    elif args.command == "version":
        commands.version()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
