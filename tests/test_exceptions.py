from python import (
    DFTToolkitError,
    ParserError,
    InvalidFileError,
)


def test_exceptions():

    assert issubclass(ParserError, DFTToolkitError)

    assert issubclass(
        InvalidFileError,
        ParserError,
    )
