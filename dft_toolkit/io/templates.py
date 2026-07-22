"""
=========================================================
DFT Toolkit for VASP
Template Manager
=========================================================
"""

import shutil
from pathlib import Path

from dft_toolkit.core.config import ConfigManager


class TemplateError(Exception):
    """Template related errors."""
    pass


class TemplateManager:
    """
    Manage VASP input templates.
    """

    def __init__(self):

        self.config = ConfigManager().load()

        self.root = self.config.root

        template_path = self.config.get(
            "templates.directory",
            "templates"
        )

        self.template_dir = self.root / template_path

    def _copy(self, src: Path, dst: Path, overwrite=False):

        if not src.exists():
            raise TemplateError(
                f"Template not found:\n{src}"
            )

        if dst.exists() and not overwrite:
            return

        shutil.copy2(src, dst)

    # -------------------------------------------------

    def copy_incar(
        self,
        workdir,
        name="RELAX",
        overwrite=False
    ):

        src = self.template_dir / "INCAR" / name.upper()
        dst = Path(workdir) / "INCAR"

        self._copy(src, dst, overwrite)

    # -------------------------------------------------

    def copy_kpoints(
        self,
        workdir,
        name="GAMMA",
        overwrite=False
    ):

        src = self.template_dir / "KPOINTS" / name.upper()
        dst = Path(workdir) / "KPOINTS"

        self._copy(src, dst, overwrite)

    # -------------------------------------------------

    def template_exists(
        self,
        category,
        name
    ):

        path = self.template_dir / category / name.upper()

        return path.exists()
