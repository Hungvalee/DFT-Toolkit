import re

from .base import BaseParser


class POTCARParser(BaseParser):
    """
    Parser for VASP POTCAR metadata.
    """

    def parse(self):

        data = {
            "potentials": [],
            "elements": [],
            "titles": [],
            "enmax": [],
            "enmin": [],
        }

        current = {}

        for line in self.lines:

            line = line.strip()

            if line.startswith("TITEL"):

                if current:
                    data["potentials"].append(current)

                title = line.split("=", 1)[1].strip()

                current = {
                    "title": title
                }

                data["titles"].append(title)

                parts = title.split()

                if len(parts) >= 2:
                    data["elements"].append(parts[1])

            elif line.startswith("ENMAX"):

                m = re.search(
                    r'ENMAX\s*=\s*([0-9.]+).*ENMIN\s*=\s*([0-9.]+)',
                    line
                )

                if m:
                    current["ENMAX"] = float(m.group(1))
                    current["ENMIN"] = float(m.group(2))

                    data["enmax"].append(float(m.group(1)))
                    data["enmin"].append(float(m.group(2)))

        if current:
            data["potentials"].append(current)

        return data
