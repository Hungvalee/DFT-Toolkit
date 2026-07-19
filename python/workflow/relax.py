"""
=========================================================
DFT Toolkit for VASP
Geometry Relaxation Workflow
=========================================================
"""

from python.workflow.base import BaseWorkflow


class RelaxWorkflow(BaseWorkflow):
    """
    Geometry optimization workflow.
    """

    REQUIRED_FILES = [
        "POSCAR",
        "POTCAR",
    ]

    def __init__(self, workdir="."):
        super().__init__(workdir)
        self.templates = TemplateManager()

    def prepare(self):
        """
        Prepare geometry optimization.
        """

        self.logger.info("=" * 60)
        self.logger.info("Geometry Relaxation")
        self.logger.info("=" * 60)

        incar = self.workdir / "INCAR"

        if not incar.exists():
            self.logger.info("INCAR not found.")
            self.logger.info("Copying RELAX template...")
            self.templates.copy_incar(
                self.workdir,
                "RELAX"
            )

        kpoints = self.workdir / "KPOINTS"

        if not kpoints.exists():
            self.logger.info("KPOINTS not found.")
            self.logger.info("Copying GAMMA template...")
            self.templates.copy_kpoints(
                self.workdir,
                "GAMMA"
            )

        self.validate()

    def run(self):
        """
        Execute geometry optimization.
        """

        self.prepare()

        self.logger.info("Starting geometry optimization...")

        self.run_vasp()

        self.postprocess()

    def postprocess(self):
        """
        Validate calculation results.
        """

        self.logger.info("Checking calculation results...")

        if self.check_outcar():
            self.logger.info(
                "Geometry optimization completed successfully."
            )
        else:
            self.logger.warning(
                "Geometry optimization finished with warnings."
            )
