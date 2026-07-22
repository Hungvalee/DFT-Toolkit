import json


class JSONReportWriter:
    """
    Write a report dictionary to a JSON file.
    """

    def write(self, report, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        return filename
