"""
=========================================================
DFT Toolkit
Density of States Plotter
=========================================================
"""

import matplotlib.pyplot as plt


class DOSPlotter:

    def __init__(self, parser):

        self.parser = parser

        self.figure = None
        self.axes = None

        self.linewidth = 1.0

        self.title = None

        self.ymin = None
        self.ymax = None

    # -------------------------------------------------

    def set_linewidth(self, value):

        self.linewidth = float(value)

        return self

    # -------------------------------------------------

    def set_title(self, title):

        self.title = str(title)

        return self

    # -------------------------------------------------

    def set_ylim(self, ymin, ymax):

        self.ymin = ymin
        self.ymax = ymax

        return self


    # -------------------------------------------------

    def show_grid(self,enable=True):

        self.grid=bool(enable)

        return self

    # -------------------------------------------------

    def set_fermi_alpha(self,value):

        self.fermi_alpha=float(value)

        return self


    # -------------------------------------------------

    def set_xlim(self, xmin, xmax):

        self.xmin = float(xmin)
        self.xmax = float(xmax)

        return self

    # -------------------------------------------------

    def plot(self):

        self.figure, self.axes = plt.subplots(figsize=(6,6))

        self.axes.plot(
            self.parser.shifted_energy,
            self.parser.total_dos,
            linewidth=self.linewidth
        )

        self.axes.axvline(
            0.0,
            linestyle="--",
            linewidth=0.8
        )

        if self.ymin is not None:

            self.axes.set_ylim(
                self.ymin,
                self.ymax
            )

        self.axes.set_xlabel("Energy (eV)")
        self.axes.set_ylabel("DOS")

        self.axes.tick_params(
            direction="in",
            top=True,
            right=True
        )

        self.axes.margins(x=0)

        if self.grid:

            self.axes.grid(
                linestyle=":",
                linewidth=0.4,
                alpha=0.5
            )

        if self.title is not None:
            self.axes.set_title(self.title)

        return self

    # -------------------------------------------------

    def save(self, filename="dos.png", dpi=300):

        self.figure.savefig(
            filename,
            dpi=dpi,
            bbox_inches="tight"
        )

        return self

    # -------------------------------------------------

    def show(self):

        plt.show()

