class DFTToolkitError(Exception):
    """Base exception for DFT-Toolkit."""


class ParserError(DFTToolkitError):
    """Raised when a parser cannot read a file."""


class InvalidFileError(ParserError):
    """Raised when an input file has an invalid format."""
