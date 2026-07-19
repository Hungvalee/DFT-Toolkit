"""
=========================================================
DFT Toolkit for VASP
INCAR Generator
=========================================================
"""

from python.io.base_input import BaseInput


class INCARGenerator(BaseInput):
    """
    Generate and modify VASP INCAR files.
    """

    TEMPLATE_SUBDIR = "INCAR"

    def __init__(self):
        super().__init__()

    def relax(self):
        return self.load_template("RELAX")

    def scf(self):
        return self.load_template("SCF")

    def dos(self):
        return self.load_template("DOS")

    def band(self):
        return self.load_template("BAND")
