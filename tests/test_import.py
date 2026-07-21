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

def test_dos():
    from python import DOS

def test_bandgap_analyzer():
    from python import BandGapAnalyzer

def test_bandgap_result():
    from python import BandGapResult

def test_electronic_structure_report():
    from python import ElectronicStructureReport

def test_json_report_writer():
    from python import JSONReportWriter

def test_csv_report_writer():
    from python import CSVReportWriter

def test_incar():
    from python import INCARParser

def test_kpoints_parser():
    from python import KPOINTSParser
