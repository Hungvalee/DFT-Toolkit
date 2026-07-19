from pathlib import Path
import yaml


class ConfigError(Exception):
    """Raised when configuration is invalid."""
    pass


class ConfigManager:

    DEFAULT_FILE = (
        Path(__file__).resolve().parents[2]
        / "config"
        / "settings.yaml"
    )

    def __init__(self, filename=None):

        self.filename = (
            Path(filename)
            if filename
            else self.DEFAULT_FILE
        )

        self.data = {}

    @property
    def root(self):
        return self.filename.parent.parent

    @property
    def config_dir(self):
        return self.filename.parent

    def load(self):

        if not self.filename.exists():
            raise ConfigError(
                f"Configuration file not found:\n{self.filename}"
            )

        with open(self.filename, "r") as f:
            self.data = yaml.safe_load(f) or {}

        return self

    def reload(self):
        return self.load()

    def save(self):

        with open(self.filename, "w") as f:
            yaml.safe_dump(
                self.data,
                f,
                sort_keys=False
            )

    def get(self, key, default=None):

        value = self.data

        for part in key.split("."):

            if not isinstance(value, dict):
                return default

            if part not in value:
                return default

            value = value[part]

        return value

    def exists(self, key):

        return self.get(key, None) is not None

    def require(self, key):

        value = self.get(key)

        if value is None:
            raise ConfigError(
                f"Missing configuration:\n{key}"
            )

        return value

    def set(self, key, value):

        parts = key.split(".")

        d = self.data

        for p in parts[:-1]:
            d = d.setdefault(p, {})

        d[parts[-1]] = value

    def section(self, name):

        value = self.get(name)

        if value is None:
            return {}

        if not isinstance(value, dict):
            raise ConfigError(
                f"{name} is not a section."
            )

        return value
