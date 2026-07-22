import numpy as np


class ChargeDifferenceAnalyzer:
    """
    Compute charge density difference:

        Δρ = ρ_total − ρ_A − ρ_B
    """

    def __init__(self, total, part_a, part_b):

        if total.grid != part_a.grid or total.grid != part_b.grid:
            raise ValueError("Charge grids are not compatible")

        self.total = total
        self.part_a = part_a
        self.part_b = part_b

    def difference(self):

        return (
            self.total.charge
            - self.part_a.charge
            - self.part_b.charge
        )

    def min(self):

        return float(np.min(self.difference()))

    def max(self):

        return float(np.max(self.difference()))

    def mean(self):

        return float(np.mean(self.difference()))
