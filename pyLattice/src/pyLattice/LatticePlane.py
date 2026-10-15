import numpy as np
from .LatticeIndex import LatticeIndex

class LatticePlane:

    def __init__(self, index):
        self.index = LatticeIndex(index)
        self.hkl = self.index.reduce()
        self.abc = self.index.invert()

    def __eq__(self, other):
        return (np.array_equal(self.hkl, other.hkl)
                and np.array_equal(self.abc, other.abc))

    def __call__(self, points: np.ndarray, d: float = 0.0):
        return np.array(d - points @ self.coeff())

    def coeff(self):
        return np.array([0 if i == 0 else 1/i for i in self.abc])

    def ncell(self):
        return np.array([1 if i == 0 else 1*i for i in self.abc])
