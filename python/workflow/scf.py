"""
=========================================================
DFT Toolkit for VASP
SCF Workflow
=========================================================
"""

from pathlib import Path

from python.workflow.base import BaseWorkflow
from python.io.incar import INCARGenerator
from python.io.kpoints import KPOINTSGenerator
from python.io.potcar import POTCARManager


class SCFWorkflow(BaseWorkflow):
    """
    Self-consistent field workflow.
    """

    def __init__(self):

        super().__init__()

        self.incar = INCARGenerator()
        self.kpoints = KPOINTSGenerator()
        self.potcar = POTCARManager()

    # -----------------------------------------------------

    def prepare(self):

        self.logger.info("Preparing SCF calculation")

        self.validate()

        if not Path("POSCAR").exists():
            raise FileNotFoundError("POSCAR not found.")

        #
        # INCAR
        #
        try:
            self.incar.load_template("scf")
        except Exception:
            pass

        try:
            self.incar.save("INCAR")
        except Exception:
            pass

        #
        # KPOINTS
        #
        try:
            self.kpoints.gamma(9)
        except Exception:
            pass

        try:
            self.kpoints.save("KPOINTS")
        except Exception:
            pass

        #
        # POTCAR
        #
        try:
            self.potcar.from_poscar("POSCAR")
        except Exception:
            pass

        self.logger.info("SCF input files prepared.")

    # -----------------------------------------------------

    def run(self):

        self.prepare()

        self.logger.info("Running VASP...")

        self.run_vasp()

        self.check_outcar()

    # -----------------------------------------------------

    def report(self):

        print()
        print("=" * 50)
        print("SCF Workflow")
        print("=" * 50)

        print("Working directory :", Path.cwd())
        print("POSCAR            :", Path("POSCAR").exists())
        print("INCAR             :", Path("INCAR").exists())
        print("KPOINTS           :", Path("KPOINTS").exists())
        print("POTCAR            :", Path("POTCAR").exists())
        print("OUTCAR            :", Path("OUTCAR").exists())

        print("=" * 50)

    # -----------------------------------------------------

    def run_all(self):

        self.run()

        self.report()
