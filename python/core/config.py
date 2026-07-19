"""
=========================================================
DFT Toolkit for VASP
Configuration Manager
=========================================================
"""

from pathlib import Path
import yaml


class ConfigError(Exception):
    """Configuration related errors."""
    pass


class Config:
    def __init__(self, filename="config/settings.yaml"):
        self.root = Path(__file__).resolve().parents[2]
        self.file = self.root / filename
        self.data = {}

    def load(self):
        if not self.file.exists():
            raise ConfigError(
                f"Configuration file not found:\n{self.file}"
            )

        with self.file.open("r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f) or {}

        return self.data

    def get(self, *keys, default=None):
        value = self.data

        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default

    def show(self):
        import pprint
        pprint.pprint(self.data)


_config = Config()


def load_config():
    """Load configuration file."""
    return _config.load()


def get_value(*keys, default=None):
    """Return configuration value."""

    if not _config.data:
        _config.load()

    return _config.get(*keys, default=default)


if __name__ == "__main__":

    load_config()

    print("=" * 60)
    print("DFT Toolkit Configuration")
    print("=" * 60)

    _config.show()

    print()
    print("VASP :", get_value("vasp", "executable"))
    print("MPI  :", get_value("mpi", "executable"))
