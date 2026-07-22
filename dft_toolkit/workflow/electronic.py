"""
=========================================================
DFT Toolkit for VASP
Electronic Structure Workflow
=========================================================
"""

from pathlib import Path
import shutil

from dft_toolkit.workflow.base import BaseWorkflow


class ElectronicStructureWorkflow(BaseWorkflow):
    """
    Base class for electronic-structure calculations
    such as Band Structure and Density of States.
    """

    def __init__(self):

        super().__init__()

    # -----------------------------------------------------

    def check_scf(self):

        required = [
            "CHGCAR",
            "WAVECAR",
            "CONTCAR",
            "OUTCAR",
        ]

        missing = [
            f for f in required
            if not Path(f).exists()
        ]

        if missing:
            raise FileNotFoundError(
                "Missing SCF files: " + ", ".join(missing)
            )

        self.logger.info("SCF calculation verified.")

    # -----------------------------------------------------

    def copy_from_scf(self, source="."):

        source = Path(source)

        files = [
            "CHGCAR",
            "WAVECAR",
            "CONTCAR",
            "POTCAR",
        ]

        for f in files:

            src = source / f

            if src.exists():

                shutil.copy2(src, f)

        self.logger.info("Copied SCF files.")

    # -----------------------------------------------------

    def restart(self):

        if Path("CONTCAR").exists():

            shutil.copy2("CONTCAR", "POSCAR")

            self.logger.info(
                "Restart structure prepared."
            )

    # -----------------------------------------------------

    def report(self):

        print()
        print("=" * 50)
        print("Electronic Structure Workflow")
        print("=" * 50)

        for f in [
            "POSCAR",
            "CONTCAR",
            "CHGCAR",
            "WAVECAR",
            "POTCAR",
            "OUTCAR",
        ]:

            print(f"{f:<12}: {Path(f).exists()}")

        print("=" * 50)

