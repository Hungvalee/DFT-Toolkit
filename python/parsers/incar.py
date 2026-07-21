from .base import BaseParser


class INCARParser(BaseParser):
    """
    Parser for VASP INCAR files.
    """

    def parse(self):
        params = {}

        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.split("#")[0]
                line = line.split("!")[0]
                line = line.strip()

                if not line or "=" not in line:
                    continue

                key, value = line.split("=", 1)

                params[key.strip()] = value.strip()

        return params
