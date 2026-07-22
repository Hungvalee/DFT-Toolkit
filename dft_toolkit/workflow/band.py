"""
=========================================================
DFT Toolkit for VASP
Band Structure Workflow
=========================================================
"""

from pathlib import Path

from dft_toolkit.workflow.electronic import ElectronicStructureWorkflow
from dft_toolkit.io.incar import INCARGenerator
from dft_toolkit.io.kpoints import KPOINTSGenerator


class BandWorkflow(ElectronicStructureWorkflow):
    """
    Workflow for non-self-consistent band structure calculations.
    """

    def __init__(self):

        super().__init__()

        self.incar = INCARGenerator()
        self.kpoints = KPOINTSGenerator()

        self.kpath = None
        self.divisions = 40

    # -------------------------------------------------

    def generate_kpath(self, path, divisions=40):
        """
        Define high-symmetry k-point path.
        """

        self.kpath = path
        self.divisions = divisions

        return self

    # -------------------------------------------------

    def prepare(self):

        self.check_scf()

        self.incar.band()

        self.incar.save("INCAR")

        if self.kpath is None:

            raise RuntimeError(
                "High-symmetry k-path has not been defined."
            )

        self.kpoints.line_mode(
            divisions=self.divisions,
            path=self.kpath
        )

        self.kpoints.save("KPOINTS")

        self.logger.info(
            "Band calculation input prepared."
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
        print("Band Structure Workflow")
        print("=" * 60)

        for f in [
            "INCAR",
            "KPOINTS",
            "CHGCAR",
            "WAVECAR",
            "EIGENVAL",
            "OUTCAR",
        ]:

            print(f"{f:<12}: {Path(f).exists()}")

        print("=" * 60)

