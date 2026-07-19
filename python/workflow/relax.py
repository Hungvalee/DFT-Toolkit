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
        "INCAR",
        "KPOINTS",
        "POTCAR",
    ]

    def prepare(self):
        """
        Validate all input files before running VASP.
        """
        self.logger.info("=" * 60)
        self.logger.info("Geometry Relaxation")
        self.logger.info("=" * 60)

        self.validate()

    def run(self):
        """
        Execute geometry optimization.
        """
        self.prepare()

        self.logger.info("Starting VASP geometry optimization...")

        self.run_vasp()

        self.postprocess()

    def postprocess(self):
        """
        Validate calculation results.
        """
        self.logger.info("Checking calculation results...")

        if self.check_outcar():
            self.logger.info("Geometry optimization completed successfully.")
        else:
            self.logger.warning(
                "Geometry optimization finished with warnings."
            )
