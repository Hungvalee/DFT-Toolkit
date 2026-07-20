"""
=========================================================
DFT Toolkit for VASP
Density of States Workflow
=========================================================
"""

from pathlib import Path

from python.workflow.electronic import ElectronicStructureWorkflow
from python.io.incar import INCARGenerator
from python.io.kpoints import KPOINTSGenerator


class DOSWorkflow(ElectronicStructureWorkflow):
    """
    Workflow for density of states calculations.
    """

    def __init__(self):

        super().__init__()

        self.incar = INCARGenerator()
        self.kpoints = KPOINTSGenerator()

        self.mesh = (9, 9, 9)

    # -------------------------------------------------

    def set_mesh(self, nx, ny, nz):

        self.mesh = (nx, ny, nz)

        return self

    # -------------------------------------------------

    def prepare(self):

        self.check_scf()

        self.incar.dos()

        self.incar.save("INCAR")

        self.kpoints.gamma(
            self.mesh[0],
            self.mesh[1],
            self.mesh[2]
        )

        self.kpoints.save("KPOINTS")

        self.logger.info(
            "DOS calculation input prepared."
        )

        return self

    # -------------------------------------------------

    def run(self):

        self.prepare()

        self.run_vasp()

        self.check_outcar()

        return self

    # -------------------------------------------------

    def report(self):

        print()
        print("=" * 60)
        print("Density of States Workflow")
        print("=" * 60)

        for f in [
            "INCAR",
            "KPOINTS",
            "DOSCAR",
            "CHGCAR",
            "WAVECAR",
            "OUTCAR",
        ]:

            print(f"{f:<12}: {Path(f).exists()}")

        print("=" * 60)

