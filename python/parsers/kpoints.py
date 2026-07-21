class KPOINTSParser:
    """
    Parser for VASP KPOINTS files.
    """

    def __init__(self):
        self.filename = None

    def read(self, filename):
        self.filename = filename
        return self

    def parse(self):

        with open(self.filename, "r", encoding="utf-8") as f:
            lines = [
                line.strip()
                for line in f
                if line.strip()
            ]

        result = {
            "comment": lines[0],
            "num_kpoints": int(lines[1]),
            "mode": lines[2],
        }

        if lines[2].lower().startswith("g"):
            result["mesh"] = list(map(int, lines[3].split()))
            result["shift"] = list(map(float, lines[4].split()))

        return result
