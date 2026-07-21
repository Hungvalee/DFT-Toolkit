class INCARParser:
    """
    Parser for VASP INCAR files.
    """

    def __init__(self):
        self.filename = None

    def read(self, filename):
        self.filename = filename
        return self

    def parse(self):
        params = {}

        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.split("#")[0]
                line = line.split("!")[0]
                line = line.strip()

                if not line or "=" not in line:
                    continue

                key, value = line.split("=", 1)

                params[key.strip()] = value.strip()

        return params
