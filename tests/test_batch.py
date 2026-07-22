from pathlib import Path

from dft_toolkit import scan_vasp_directories


def test_batch_scan():

    dirs = scan_vasp_directories(Path("tests/data"))

    assert isinstance(dirs, list)
