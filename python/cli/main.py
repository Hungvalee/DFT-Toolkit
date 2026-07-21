import argparse

from python import (
    OUTCARParser,
    EIGENVALParser,
    PROCARParser,
    BandStructure,
    ElectronicStructureReport,
)


def main():

    parser = argparse.ArgumentParser(
        prog="dft-toolkit"
    )

    sub = parser.add_subparsers(dest="command")

    report = sub.add_parser("report")

    report.add_argument("--outcar", required=True)
    report.add_argument("--eigenval", required=True)
    report.add_argument("--procar", required=True)

    args = parser.parse_args()

    if args.command == "report":

        outcar = OUTCARParser().read(args.outcar).parse()
        eigen = EIGENVALParser().read(args.eigenval).parse()
        procar = PROCARParser().read(args.procar).parse()

        bs = BandStructure.from_vasp(
            outcar,
            eigen,
            procar,
        )

        result = ElectronicStructureReport(bs).as_dict()

        for key, value in result.items():
            print(f"{key:15s}: {value}")


if __name__ == "__main__":
    main()
