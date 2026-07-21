from pathlib import Path


class BaseParser:
    """
    Base class for all parsers.

    Backward compatible:
        self.filename
        self.path
        self.lines
    """

    def __init__(self):
        self.filename = None
        self.lines = []

    def read(self, filename):

        self.filename = Path(filename)

        with open(self.filename, "r", encoding="utf-8") as f:
            self.lines = f.readlines()

        return self

    @property
    def path(self):
        return self.filename
