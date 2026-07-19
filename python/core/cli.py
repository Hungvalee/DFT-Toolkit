"""
=========================================================
DFT Toolkit for VASP
Command Line Interface
=========================================================
"""

import argparse
import shutil
import subprocess
from pathlib import Path

from python.core.version import show_version


ROOT = Path(__file__).resolve().parents[2]


def cmd_version(args):
    """Show version information."""
    show_version()


def cmd_doctor(args):
    """Check required software."""

    print("=" * 60)
    print("DFT Toolkit Environment Check")
    print("=" * 60)

    programs = {
        "python3": "python3",
        "mpirun": "mpirun",
        "phonopy": "phonopy",
        "vaspkit": "vaspkit",
    }

    for name, exe in programs.items():
        path = shutil.which(exe)
        status = "OK" if path else "NOT FOUND"
        print(f"{name:<12}: {status}")

    print("=" * 60)


def cmd_init(args):
    """Create a new project."""

    project = Path(args.project)

    if project.exists():
        print(f"Project '{project}' already exists.")
        return

    subprocess.run(
        [
            "bash",
            str(ROOT / "scripts" / "create_project.sh"),
            str(project),
        ],
        check=True,
    )


def build_parser():

    parser = argparse.ArgumentParser(
        prog="dft",
        description="DFT Toolkit for VASP"
    )

    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("version", help="Show version")
    p.set_defaults(func=cmd_version)

    p = sub.add_parser("doctor", help="Check environment")
    p.set_defaults(func=cmd_doctor)

    p = sub.add_parser("init", help="Create project")
    p.add_argument("project")
    p.set_defaults(func=cmd_init)

    return parser


def main():

    parser = build_parser()

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
