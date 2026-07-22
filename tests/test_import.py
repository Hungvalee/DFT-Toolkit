"""
Basic import tests for dft_toolkit.
"""

import dft_toolkit


def test_package_import():
    """Package can be imported."""
    assert dft_toolkit is not None


def test_version_exists():
    """Package defines a version string."""
    assert hasattr(dft_toolkit, "__version__")
    assert isinstance(dft_toolkit.__version__, str)
