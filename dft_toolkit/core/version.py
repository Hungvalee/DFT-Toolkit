"""
=========================================================
DFT Toolkit for VASP
Version Manager
=========================================================
"""

from pathlib import Path
import yaml


class VersionError(Exception):
    """Version file related errors."""
    pass


class Version:

    def __init__(self, filename="config/version.yaml"):

        self.root = Path(__file__).resolve().parents[2]
        self.file = self.root / filename
        self.data = {}

    def load(self):

        if not self.file.exists():
            raise VersionError(
                f"Version file not found:\n{self.file}"
            )

        with self.file.open("r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f) or {}

        return self.data

    def get(self, key, default=None):

        if not self.data:
            self.load()

        return self.data.get(key, default)

    def show(self):

        if not self.data:
            self.load()

        print("=" * 60)
        print(f"{self.get('name', 'DFT Toolkit')}")
        print("=" * 60)
        print(f"Version : {self.get('version', 'Unknown')}")
        print(f"Release : {self.get('release', '-')}")
        print(f"Author  : {self.get('author', '-')}")
        print(f"License : {self.get('license', '-')}")
        print("=" * 60)


_version = Version()


def load_version():
    """Load version information."""
    return _version.load()


def get_version(key, default=None):
    """Return a version field."""
    return _version.get(key, default)


def show_version():
    """Display version information."""
    _version.show()


if __name__ == "__main__":
    show_version()
