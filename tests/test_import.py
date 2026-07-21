"""
Basic import tests.
"""

import python


def test_package_import():

    assert python is not None


def test_procar():

    from python import PROCARParser

    assert PROCARParser is not None


def test_eigenval():

    from python import EIGENVALParser

    assert EIGENVALParser is not None


def test_doscar():

    from python import DOSCARParser

    assert DOSCARParser is not None


def test_outcar():

    from python import OUTCARParser

    assert OUTCARParser is not None

def test_xdatcar():
    from python import XDATCARParser

def test_chgcar():
    from python import CHGCARParser

def test_locpot():
    from python import LOCPOTParser

def test_work_function():
    from python import WorkFunctionAnalyzer
