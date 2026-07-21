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

def test_bandstructure():
    from python import BandStructure

def test_effective_mass():
    from python import EffectiveMassAnalyzer

def test_charge_difference():
    from python import ChargeDifferenceAnalyzer

def test_density_profile():
    from python import DensityProfileAnalyzer

def test_profile_writer():
    from python import ProfileWriter

def test_bandstructure_writer():
    from python import BandStructureWriter

def test_kpath():
    from python import KPath
