import csv


class CSVReportWriter:
    """
    Write a report dictionary to a CSV file.
    """

    def write(self, report, filename):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(["Property", "Value"])

            for key, value in report.items():
                writer.writerow([key, value])

        return filename
