from python.cli.main import main


def test_cli_import():
    assert callable(main)
