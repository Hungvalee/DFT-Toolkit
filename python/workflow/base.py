"""
=========================================================
DFT Toolkit for VASP
Base Workflow
=========================================================
"""

from pathlib import Path
import shutil
import subprocess

from python.core.config import get_value
from python.core.logger import get_logger
from python.io.templates import TemplateManager


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

        self.templates = TemplateManager()

        self.vasp = get_value("vasp", "executable")
        self.mpirun = get_value("mpi", "executable")
        self.nproc = get_value("mpi", "processes", default=4)

    # =====================================================
    # Validators
    # =====================================================

    def check_required_files(self):

        missing = []

        for name in self.REQUIRED_FILES:

            path = self.workdir / name

            if not path.exists():
                missing.append(name)

        if missing:
            raise WorkflowError(
                "Missing required files:\n  " +
                "\n  ".join(missing)
            )

        self.logger.info("Required files found.")

    def check_empty_files(self):

        empty = []

        for name in self.REQUIRED_FILES:

            path = self.workdir / name

            if path.exists() and path.stat().st_size == 0:
                empty.append(name)

        if empty:
            raise WorkflowError(
                "Empty input files:\n  " +
                "\n  ".join(empty)
            )

        self.logger.info("Input files are not empty.")

    def check_poscar(self):

        path = self.workdir / "POSCAR"

        if not path.exists():
            return

        lines = path.read_text(errors="ignore").splitlines()

        if len(lines) < 8:
            raise WorkflowError(
                "Invalid POSCAR: fewer than 8 lines."
            )

        self.logger.info("POSCAR validated.")

    def check_incar(self):

        path = self.workdir / "INCAR"

        if not path.exists():
            return

        text = path.read_text(errors="ignore").strip()

        if not text:
            raise WorkflowError("INCAR is empty.")

        self.logger.info("INCAR validated.")

    def check_kpoints(self):

        path = self.workdir / "KPOINTS"

        if not path.exists():
            return

        lines = path.read_text(errors="ignore").splitlines()

        if len(lines) < 4:
            raise WorkflowError(
                "Invalid KPOINTS."
            )

        self.logger.info("KPOINTS validated.")

    def check_potcar(self):

        path = self.workdir / "POTCAR"

        if not path.exists():
            return

        text = path.read_text(errors="ignore")

        if "PAW" not in text:
            raise WorkflowError(
                "Invalid POTCAR."
            )

        self.logger.info("POTCAR validated.")

    def check_vasp(self):

        if not self.vasp:
            raise WorkflowError(
                "VASP executable is not configured."
            )

        if not Path(self.vasp).exists():
            raise WorkflowError(
                f"VASP executable not found:\n{self.vasp}"
            )

        self.logger.info("VASP executable found.")

    def check_mpirun(self):

        if not self.mpirun:
            raise WorkflowError(
                "MPI executable is not configured."
            )

        if shutil.which(self.mpirun):
            self.logger.info("MPI executable found.")
            return

        if Path(self.mpirun).exists():
            self.logger.info("MPI executable found.")
            return

        raise WorkflowError(
            f"MPI executable not found:\n{self.mpirun}"
        )

    def validate(self):

        self.logger.info("Validating workflow...")

        self.check_required_files()
        self.check_empty_files()

        self.check_poscar()
        self.check_incar()
        self.check_kpoints()
        self.check_potcar()

        self.check_vasp()
        self.check_mpirun()

        self.logger.info("Validation completed successfully.")

    # =====================================================
    # Execution
    # =====================================================

    def run_command(self, cmd):

        self.logger.info("Running command:")
        self.logger.info("  %s", " ".join(cmd))

        result = subprocess.run(
            cmd,
            cwd=self.workdir,
        )

        if result.returncode != 0:
            raise WorkflowError(
                f"Command failed (exit code {result.returncode})"
            )

        return result

    def run_vasp(self):

        cmd = [
            self.mpirun,
            "-np",
            str(self.nproc),
            self.vasp,
        ]

        self.run_command(cmd)

        self.logger.info("VASP finished successfully.")

    def check_outcar(self):

        outcar = self.workdir / "OUTCAR"

        if not outcar.exists():
            raise WorkflowError("OUTCAR not found.")

        text = outcar.read_text(errors="ignore")

        if "General timing and accounting informations" not in text:
            self.logger.warning(
                "Calculation may not have finished normally."
            )
            return False

        self.logger.info("OUTCAR validated.")

        return True

    # =====================================================
    # Abstract API
    # =====================================================

    def prepare(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def postprocess(self):
        raise NotImplementedError
