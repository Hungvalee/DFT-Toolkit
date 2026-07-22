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

        #
        # Default x-axis
        #
        self.x = np.arange(parser.nkpts)

    # -------------------------------------------------

    def set_kdistance(self, x):

        x = np.asarray(x)

        if len(x) != self.parser.nkpts:
            raise ValueError("Length mismatch.")

        self.x = x

        return self

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
                c=color,
                alpha=alpha,
                linewidths=0,
                zorder=2
            )

        return self

    # -------------------------------------------------

    def add_fermi(self,
                  energy=0.0,
                  **kwargs):

        defaults = {
            "color": "gray",
            "linestyle": "--",
            "linewidth": 0.8
        }

        defaults.update(kwargs)

        self.ax.axhline(
            energy,
            **defaults
        )

        return self

    # -------------------------------------------------

    def add_vertical_lines(self,
                           positions,
                           **kwargs):

        defaults = {
            "color": "gray",
            "linewidth": 0.5
        }

        defaults.update(kwargs)

        for p in positions:
            self.ax.axvline(p, **defaults)

        return self

    # -------------------------------------------------

    def set_xticks(self,
                   positions,
                   labels):

        self.ax.set_xticks(positions)
        self.ax.set_xticklabels(labels)

        return self

    # -------------------------------------------------

    def xlabel(self, text):

        self.ax.set_xlabel(text)

        return self

    def ylabel(self, text):

        self.ax.set_ylabel(text)

        return self

    def title(self, text):

        self.ax.set_title(text)

        return self

    # -------------------------------------------------

    def set_xlim(self, xmin, xmax):

        self.ax.set_xlim(xmin, xmax)

        return self

    def set_ylim(self, ymin, ymax):

        self.ax.set_ylim(ymin, ymax)

        return self

    # -------------------------------------------------

    def grid(self):

        self.ax.grid(alpha=0.3)

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
            dpi=300,
            bbox_inches="tight"
        )

    # -------------------------------------------------

    def show(self):

        plt.show()

