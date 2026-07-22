from pathlib import Path


class BaseParser:
    """
    Base class for all VASP parsers.
    """

    def __init__(self):
        self.filename = None
        self.lines = []

    def read(self, filename):

        self.filename = Path(filename)

        if not self.filename.exists():
            raise FileNotFoundError(
                f"Input file not found: {self.filename}"
            )

        if self.filename.is_dir():
            raise IsADirectoryError(
                f"Expected a file but got a directory: {self.filename}"
            )

        with open(self.filename, "r", encoding="utf-8") as f:
            self.lines = f.readlines()

        return self

    @property
    def path(self):
        return self.filename
