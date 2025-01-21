import numpy as np


class LatticeIndexError(ValueError):
    pass


class LatticeIndex(np.ndarray):

    def __new__(cls,
                index: list
                ):
        obj = np.asarray(index, dtype=int).view(cls)
        return obj

    def __array_finalize__(self, obj = None):
        if obj is None: return

    @staticmethod
    def GCD(self):
        return int(np.gcd.reduce(np.abs(self[self != 0])))

    @staticmethod
    def LCM(self):
        return int(np.lcm.reduce(np.abs(self[self != 0])))

    def reduce(self):
        gcd = LatticeIndex.GCD(self)
        reduced = np.array([i/gcd for i in self]).astype(int)
        return reduced.view(LatticeIndex)

    def invert(self):
        lcm = LatticeIndex.LCM(self)
        inverse = np.array([0 if i==0 else lcm/i for i in self]).astype(int)
        return inverse.view(LatticeIndex)

    def ones(self):
        return np.array([1 if i == 0 else i for i in self]).view(LatticeIndex)
