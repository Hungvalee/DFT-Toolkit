from dft_toolkit.cli.main import main


def test_cli_import():
    assert callable(main)
