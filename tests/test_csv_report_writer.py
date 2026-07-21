from python import CSVReportWriter


def test_csv_writer(tmp_path):

    report = {
        "band_gap": 1.42,
        "gap_type": "direct",
    }

    outfile = tmp_path / "report.csv"

    CSVReportWriter().write(report, outfile)

    assert outfile.exists()

    text = outfile.read_text()

    assert "band_gap" in text
    assert "gap_type" in text
