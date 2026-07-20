"""
=========================================================
DFT Toolkit
Base Parser
=========================================================
"""

from pathlib import Path


class ParserError(Exception):
    """Parser related errors."""
    pass


class BaseParser:

    def __init__(self):

        self.filename = None
        self.lines = []

    # -------------------------------------------------

    def read(self, filename):

        path = Path(filename)

        if not path.exists():
            raise ParserError(f"File not found:\n{path}")

        self.filename = str(path)

        with path.open(
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            self.lines = f.readlines()

        return self

    # -------------------------------------------------

    @property
    def nlines(self):

        return len(self.lines)
