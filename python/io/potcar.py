from pathlib import Path
import shutil
import yaml
from python.core.config import ConfigManager


class POTCARError(Exception):
    """POTCAR related errors."""
    pass


class POTCARManager:

    def __init__(self, library=None, mapping=None):

        self.library = None
        self.mapping = {}

        if library:
            self.set_library(library)

        if mapping:
            self.load_mapping(mapping)

    # ---------------------------------------------------------

    def load_config(self):

        cfg = ConfigManager().load()

        self.set_library(
            cfg.require("potcar.library")
        )

        self.load_mapping(
            cfg.require("potcar.mapping")
        )

        return self

    # ---------------------------------------------------------

    def load_mapping(self, filename):

        filename = Path(filename)

        if not filename.exists():
            raise POTCARError(
                f"Mapping file not found:\n{filename}"
            )

        with open(filename) as f:
            self.mapping = yaml.safe_load(f)

        return self

    # ---------------------------------------------------------

    def set_library(self, library):

        library = Path(library)

        if not library.exists():
            raise POTCARError(
                f"Library not found:\n{library}"
            )

        self.library = library

        return self

    # ---------------------------------------------------------

    def available(self):

        if self.library is None:
            raise POTCARError(
                "POTCAR library not set."
            )

        return sorted(
            d.name
            for d in self.library.iterdir()
            if (d / "POTCAR").exists()
        )

    # ---------------------------------------------------------

    def validate_mapping(self):

        missing = []

        for element, folder in self.mapping.items():

            potcar = self.library / folder / "POTCAR"

            if not potcar.exists():
                missing.append(
                    (element, folder)
                )

        return missing

    # ---------------------------------------------------------

    def info(self):

        return (
            "POTCAR Library\n"
            "--------------\n"
            f"Library : {self.library}\n"
            f"Potentials : {len(self.available())}\n"
            f"Mappings : {len(self.mapping)}"
        )

    # ---------------------------------------------------------

    def _read_elements(self, poscar):

        poscar = Path(poscar)

        if not poscar.exists():
            raise POTCARError(
                f"POSCAR not found:\n{poscar}"
            )

        lines = poscar.read_text().splitlines()

        if not lines:
            raise POTCARError(
                f"Empty POSCAR:\n{poscar}"
            )

        if len(lines) < 8:
            raise POTCARError(
                f"Invalid POSCAR format:\n{poscar}"
            )

        return lines[5].split()

    # ---------------------------------------------------------

    def _find_potential(self, element):

        folder = self.mapping.get(
            element,
            element
        )

        potcar = self.library / folder / "POTCAR"

        if not potcar.exists():
            raise POTCARError(
                f"POTCAR not found:\n{folder}"
            )

        return potcar

    # ---------------------------------------------------------

    def generate(self, elements, output="POTCAR"):

        output = Path(output)

        with output.open("wb") as fout:

            for element in elements:

                potcar = self._find_potential(
                    element
                )

                with potcar.open("rb") as fin:
                    shutil.copyfileobj(
                        fin,
                        fout
                    )

        return output

    # ---------------------------------------------------------

    def from_poscar(
        self,
        poscar="POSCAR",
        output="POTCAR"
    ):

        elements = self._read_elements(
            poscar
        )

        return self.generate(
            elements,
            output
        )

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"POTCARManager("
            f"library={self.library!r})"
        )

