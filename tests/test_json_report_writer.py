from pathlib import Path

from python import JSONReportWriter


def test_json_writer(tmp_path):

    report = {
        "band_gap": 1.42,
        "gap_type": "direct",
    }

    outfile = tmp_path / "report.json"

    JSONReportWriter().write(report, outfile)

    assert outfile.exists()

    text = outfile.read_text()

    assert '"band_gap"' in text
    assert '"gap_type"' in text
