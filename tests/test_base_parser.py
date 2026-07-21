import pytest

from python.parsers.base import BaseParser


def test_missing_file():

    with pytest.raises(FileNotFoundError):
        BaseParser().read("this_file_does_not_exist")


def test_read_existing_file():

    parser = BaseParser().read("pyproject.toml")

    assert len(parser.lines) > 0
