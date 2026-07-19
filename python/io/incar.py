"""
=========================================================
DFT Toolkit for VASP
INCAR Generator
=========================================================
"""

from pathlib import Path


class INCARError(Exception):
    """INCAR related errors."""
    pass


class INCARGenerator:
    """
    Generate and modify VASP INCAR files.
    """

    def __init__(self):

        self.parameters = {}

        self.root = Path(__file__).resolve().parents[2]
        self.template_dir = self.root / "templates" / "INCAR"

    # -------------------------------------------------

    def clear(self):
        self.parameters.clear()
        return self

    # -------------------------------------------------

    def set(self, key, value):
        self.parameters[str(key).upper()] = value
        return self

    # -------------------------------------------------

    def update(self, mapping):
        for key, value in mapping.items():
            self.set(key, value)
        return self

    # -------------------------------------------------

    def remove(self, key):
        self.parameters.pop(str(key).upper(), None)
        return self

    # -------------------------------------------------

    def get(self, key, default=None):
        return self.parameters.get(str(key).upper(), default)

    # -------------------------------------------------

    def to_dict(self):
        return dict(self.parameters)

    # -------------------------------------------------

    def _format_value(self, value):

        if isinstance(value, bool):
            return ".TRUE." if value else ".FALSE."

        if isinstance(value, float):
            return f"{value:.6E}"

        return str(value)

    # -------------------------------------------------

    def load_template(self, name):

        path = self.template_dir / name.upper()

        if not path.exists():
            raise INCARError(f"Template not found:\n{path}")

        self.clear()

        for line in path.read_text().splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            if "=" not in line:
                continue

            key, value = line.split("=", 1)

            self.parameters[key.strip().upper()] = value.strip()

        return self

    # -------------------------------------------------

    def save(self, filename):

        path = Path(filename)

        with path.open("w") as f:

            for key, value in self.parameters.items():
                f.write(
                    f"{key} = {self._format_value(value)}\n"
                )

        return self

    # -------------------------------------------------

    def __str__(self):

        lines = []

        for key, value in self.parameters.items():
            lines.append(
                f"{key} = {self._format_value(value)}"
            )

        return "\n".join(lines)

    # -------------------------------------------------

    def relax(self):
        return self.load_template("RELAX")

    def scf(self):
        return self.load_template("SCF")

    def dos(self):
        return self.load_template("DOS")

    def band(self):
        return self.load_template("BAND")
