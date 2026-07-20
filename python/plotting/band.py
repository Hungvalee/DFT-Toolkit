"""
=========================================================
DFT Toolkit
Band Structure Plotter
=========================================================
"""

import matplotlib.pyplot as plt


class BandPlotter:

    def __init__(self, parser):

        self.parser = parser

        self.figure = None
        self.axes = None

        self.fermi = 0.0

    # -------------------------------------------------

    def plot(self):

        self.figure, self.axes = plt.subplots(figsize=(6,6))

        x = range(len(self.parser))

        for band in self.parser.bands:

            y = self.parser.eigenvalues[:, band] - self.fermi

            self.axes.plot(
                x,
                y,
                linewidth=1.0
            )

        self.axes.axhline(
            0.0,
            linestyle="--"
        )

        self.axes.set_xlabel("k-point")

        self.axes.set_ylabel("Energy (eV)")

        self.axes.set_title("Band Structure")

        return self

    # -------------------------------------------------

    def save(self, filename="band.png", dpi=300):

        self.figure.savefig(
            filename,
            dpi=dpi,
            bbox_inches="tight"
        )

        return self

    # -------------------------------------------------

    def show(self):

        plt.show()

