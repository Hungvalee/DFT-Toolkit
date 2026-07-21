import argparse

from python import __version__


def main():
    parser = argparse.ArgumentParser(
        prog="dft-toolkit",
        description="DFT-Toolkit: A Python toolkit for VASP analysis"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )

    parser.parse_args()

    print("DFT-Toolkit")
    print("Use --help to see available commands.")


if __name__ == "__main__":
    main()
