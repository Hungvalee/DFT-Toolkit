from pathlib import Path

from python import (
    LOCPOTParser,
    DensityProfileAnalyzer,
    ProfileWriter,
)

DATA = Path(__file__).parent / "data" / "locpot" / "LOCPOT"


def test_profile_writer(tmp_path):

    locpot = LOCPOTParser().read(DATA).parse()

    profile = DensityProfileAnalyzer(locpot).profile_z()

    outfile = tmp_path / "profile.dat"

    ProfileWriter.write(outfile, profile)

    assert outfile.exists()

    lines = outfile.read_text().splitlines()

    assert len(lines) >= 3
