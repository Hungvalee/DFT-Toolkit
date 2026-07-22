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

        self.ymin = None
        self.ymax = None

        self.klabels = None
        self.kticks = None

        self.linewidth = 0.8
        self.title = None


    # -------------------------------------------------

    def set_fermi(self,value):

        self.fermi=float(value)

        return self

    # -------------------------------------------------

    def set_ylim(self,ymin,ymax):

        self.ymin=float(ymin)
        self.ymax=float(ymax)

        return self

    # -------------------------------------------------

    def set_kpath(self,labels,ticks):

        self.klabels=list(labels)
        self.kticks=list(ticks)

        return self


    # -------------------------------------------------

    def set_linewidth(self,value):

        self.linewidth=float(value)

        return self

    # -------------------------------------------------

    def set_title(self,title):

        self.title=str(title)

        return self

    # -------------------------------------------------

    def plot(self):

        self.figure, self.axes = plt.subplots(figsize=(6,6))

        x = range(len(self.parser))

        for band in self.parser.bands:

            y = self.parser.eigenvalues[:, band] - self.fermi

            self.axes.plot(
                x,
                y,
                linewidth=self.linewidth
            )

        self.axes.axhline(
            0.0,
            linestyle="--",
            linewidth=0.8
        )

        if self.ymin is not None:

            self.axes.set_ylim(
                self.ymin,
                self.ymax
            )

        if self.kticks is not None:

            self.axes.set_xticks(self.kticks)

            self.axes.set_xticklabels(
                self.klabels
            )

            for x in self.kticks:

                self.axes.axvline(
                    x,
                    linewidth=0.5
                )

        self.axes.tick_params(
            direction="in",
            top=True,
            right=True
        )

        self.axes.set_xlabel("")

        self.axes.set_ylabel("Energy (eV)")

        if self.title is not None:
            self.axes.set_title(self.title)

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

