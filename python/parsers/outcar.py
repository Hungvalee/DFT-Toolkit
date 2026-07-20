"""
=========================================================
DFT Toolkit
OUTCAR Parser
=========================================================
"""

import re

from python.parsers.base import BaseParser


class OUTCARParser(BaseParser):

    def __init__(self):

        super().__init__()

        self.version = None
        self.encut = None
        self.nions = None
        self.nelect = None
        self.fermi = None
        self.energy = None

    # -------------------------------------------------

    def parse(self):

        for line in self.lines:

            if self.version is None:

                m = re.search(
                    r"vasp\.(.+)",
                    line,
                    re.I
                )

                if m:
                    self.version = m.group(0).strip()

            if self.encut is None:

                m = re.search(
                    r"ENCUT *= *([0-9.]+)",
                    line
                )

                if m:
                    self.encut = float(m.group(1))

            if self.nions is None:

                m = re.search(
                    r"NIONS *= *([0-9]+)",
                    line
                )

                if m:
                    self.nions = int(m.group(1))

            if self.nelect is None:

                m = re.search(
                    r"NELECT *= *([0-9.]+)",
                    line
                )

                if m:
                    self.nelect = float(m.group(1))

            if "E-fermi" in line:

                self.fermi = float(
                    line.split()[2]
                )

            if "free  energy   TOTEN" in line:

                self.energy = float(
                    line.split()[-2]
                )

        return self

    # -------------------------------------------------

    def summary(self):

        print()

        print("="*60)

        print("OUTCAR Summary")

        print("="*60)

        print(f"Version : {self.version}")
        print(f"ENCUT   : {self.encut}")
        print(f"NIONS   : {self.nions}")
        print(f"NELECT  : {self.nelect}")
        print(f"E-fermi : {self.fermi}")
        print(f"TOTEN   : {self.energy}")

        print("="*60)
