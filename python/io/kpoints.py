"""
=========================================================
DFT Toolkit for VASP
KPOINTS Generator
=========================================================
"""

from pathlib import Path


class KPOINTSError(Exception):
    """KPOINTS related errors."""
    pass


class KPOINTSGenerator:
    """
    Generate VASP KPOINTS files.
    """

    def __init__(self):

        self.comment = "Automatic mesh"

        self.mode = "Gamma"

        self.mesh = (9, 9, 1)

        self.shift = (0, 0, 0)

    # -------------------------------------------------

    def gamma(self, nx, ny, nz):

        self.mode = "Gamma"
        self.mesh = (nx, ny, nz)

        return self

    # -------------------------------------------------

    def monkhorst(self, nx, ny, nz):

        self.mode = "Monkhorst-Pack"
        self.mesh = (nx, ny, nz)

        return self

    # -------------------------------------------------

    def offset(self, sx, sy, sz):

        self.shift = (sx, sy, sz)

        return self

    # -------------------------------------------------


    def line_mode(self, divisions=40, path=None):
        """
        Generate line-mode KPOINTS for band structure.
        """

        if path is None or len(path) < 2:
            raise ValueError(
                "path must contain at least two k-points."
            )

        self.comment = "Band Structure"

        lines = [
            self.comment,
            str(divisions),
            "Line-mode",
            "Reciprocal",
        ]

        for i in range(len(path)-1):

            label1, k1 = path[i]
            label2, k2 = path[i+1]

            lines.append(
                f"{k1[0]:10.6f} {k1[1]:10.6f} {k1[2]:10.6f} ! {label1}"
            )

            lines.append(
                f"{k2[0]:10.6f} {k2[1]:10.6f} {k2[2]:10.6f} ! {label2}"
            )

            lines.append("")

        self._line_text = "\n".join(lines)

        return self

    # -------------------------------------------------

    def save(self, filename):

        path = Path(filename)

        with path.open("w") as f:

            if hasattr(self, "_line_text"):
                f.write(self._line_text)
            else:
                f.write(f"{self.comment}\n")
                f.write("0\n")
                f.write(f"{self.mode}\n")

                f.write(
                    f"{self.mesh[0]} "
                    f"{self.mesh[1]} "
                    f"{self.mesh[2]}\n"
                )

                f.write(
                    f"{self.shift[0]} "
                    f"{self.shift[1]} "
                    f"{self.shift[2]}\n"
                )

        return self

    # -------------------------------------------------

    def __str__(self):

        return (
            f"{self.comment}\n"
            "0\n"
            f"{self.mode}\n"
            f"{self.mesh[0]} {self.mesh[1]} {self.mesh[2]}\n"
            f"{self.shift[0]} {self.shift[1]} {self.shift[2]}"
        )
