"""
=========================================================
DFT Toolkit for VASP
Base Workflow
=========================================================
"""

from pathlib import Path
import subprocess

from python.core.config import get_value
from python.core.logger import get_logger


class WorkflowError(Exception):
    """Workflow related errors."""
    pass


class BaseWorkflow:
    """
    Base class for all DFT workflows.
    """

    REQUIRED_FILES = []

    def __init__(self, workdir="."):

        self.workdir = Path(workdir).resolve()
        self.logger = get_logger(self.__class__.__name__)

        self.vasp = get_value("vasp", "executable")
        self.mpirun = get_value("mpi", "executable")
        self.nproc = get_value("mpi", "processes", default=4)

    def check_files(self):

        missing = []

        for filename in self.REQUIRED_FILES:
            if not (self.workdir / filename).exists():
                missing.append(filename)

        if missing:
            raise WorkflowError(
                "Missing required files:\n  " +
                "\n  ".join(missing)
            )

    def run_vasp(self):

        cmd = [
            self.mpirun,
            "-np",
            str(self.nproc),
            self.vasp,
        ]

        self.logger.info("Running VASP")
        self.logger.info("Command: %s", " ".join(cmd))

        result = subprocess.run(
            cmd,
            cwd=self.workdir,
        )

        if result.returncode != 0:
            raise WorkflowError("VASP terminated with errors.")

        self.logger.info("VASP finished successfully.")

    def check_outcar(self):

        outcar = self.workdir / "OUTCAR"

        if not outcar.exists():
            raise WorkflowError("OUTCAR not found.")

        text = outcar.read_text(errors="ignore")

        if "General timing and accounting informations" not in text:
            self.logger.warning("Calculation may not have finished normally.")
            return False

        self.logger.info("OUTCAR check passed.")
        return True

    def prepare(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def postprocess(self):
        raise NotImplementedError
