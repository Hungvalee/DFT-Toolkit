"""
=========================================================
DFT Toolkit
PDOS Plotter
=========================================================
"""

import matplotlib.pyplot as plt
import numpy as np


class PDOSPlotter:

    orbital_index = {
        "s": 1,
        "py": 2,
        "pz": 3,
        "px": 4,
        "dxy": 5,
        "dyz": 6,
        "dz2": 7,
        "dxz": 8,
        "dx2": 9,
    }

    def __init__(self, parser):

        self.parser = parser

        self.fig, self.ax = plt.subplots(figsize=(6, 5))

        self.xlim = None
        self.ylim = None

    # -------------------------------------------------

    def set_xlim(self, xmin, xmax):

        self.xlim = (xmin, xmax)

        return self

    # -------------------------------------------------

    def set_ylim(self, ymin, ymax):

        self.ylim = (ymin, ymax)

        return self

    # -------------------------------------------------

    def add_total(self, **kwargs):

        self.ax.plot(
            self.parser.shifted_energy,
            self.parser.total_dos,
            label="Total DOS",
            **kwargs
        )

        return self

    # -------------------------------------------------

    def add_orbital(self, atom, orbital, **kwargs):

        idx = self.orbital_index[orbital]

        energy = self.parser.pdos[atom - 1][:, 0] - self.parser.efermi

        dos = self.parser.pdos[atom - 1][:, idx]

        self.ax.plot(
            energy,
            dos,
            label=f"Atom {atom} ({orbital})",
            **kwargs
        )

        return self

    # -------------------------------------------------

    def plot(self):

        self.ax.axvline(0.0, linestyle="--", linewidth=1)

        self.ax.set_xlabel("Energy (eV)")
        self.ax.set_ylabel("Density of States")

        if self.xlim is not None:
            self.ax.set_xlim(*self.xlim)

        if self.ylim is not None:
            self.ax.set_ylim(*self.ylim)

        self.ax.legend()

        return self

    # -------------------------------------------------

    def save(self, filename):

        self.fig.tight_layout()

        self.fig.savefig(filename, dpi=300)

        return self
