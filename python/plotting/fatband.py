"""
=========================================================
DFT Toolkit
Fat Band Plotter
=========================================================
"""

import matplotlib.pyplot as plt
import numpy as np


class FatBandPlotter:

    def __init__(self, parser):

        self.parser = parser

        self.fig = None
        self.ax = None

        self.scale = 300

        self.x = np.arange(parser.nkpts)

    # -------------------------------------------------

    def set_scale(self, scale):

        self.scale = scale

        return self

    # -------------------------------------------------

    def add_band(self,
                 color="black",
                 linewidth=0.8):

        for b in range(self.parser.nbands):

            self.ax.plot(
                self.x,
                self.parser.band_energy[:, b],
                color=color,
                linewidth=linewidth,
                zorder=1
            )

        return self

    # -------------------------------------------------

    def add_orbital(self,
                    atom,
                    orbital,
                    color="red",
                    alpha=0.6):

        weight = self.parser.orbital(atom, orbital)

        for b in range(self.parser.nbands):

            self.ax.scatter(
                self.x,
                self.parser.band_energy[:, b],
                s=self.scale * weight[:, b],
                color=color,
                alpha=alpha,
                linewidths=0,
                zorder=2
            )

        return self

    # -------------------------------------------------

    def xlabel(self, label):

        self.ax.set_xlabel(label)

        return self

    # -------------------------------------------------

    def ylabel(self, label):

        self.ax.set_ylabel(label)

        return self

    # -------------------------------------------------

    def set_xlim(self, xmin, xmax):

        self.ax.set_xlim(xmin, xmax)

        return self

    # -------------------------------------------------

    def set_ylim(self, ymin, ymax):

        self.ax.set_ylim(ymin, ymax)

        return self

    # -------------------------------------------------

    def plot(self):

        self.fig, self.ax = plt.subplots(figsize=(6,5))

        return self

    # -------------------------------------------------

    def save(self, filename):

        self.fig.tight_layout()

        self.fig.savefig(
            filename,
            dpi=300
        )

    # -------------------------------------------------

    def show(self):

        plt.show()

