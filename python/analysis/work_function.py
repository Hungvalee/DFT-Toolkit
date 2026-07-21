import numpy as np


class WorkFunctionAnalyzer:

    def __init__(self, locpot):

        self.locpot = locpot

    def planar_average(self):

        return self.locpot.potential.mean(axis=(0,1))

    def vacuum_level(self):

        return self.planar_average().max()

    def work_function(self):

        return self.vacuum_level() - self.locpot.efermi
