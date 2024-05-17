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

    def gcd(self):
        return int(np.gcd.reduce(np.abs(self[self != 0])))

    def lcm(self):
        return int(np.lcm.reduce(np.abs(self[self != 0])))

    def reduce(self):
        gcd = self.gcd()
        return np.array([i/gcd for i in self]).view(LatticeIndex)

    def invert(self):
        lcm = self.lcm()
        return np.array([0 if i==0 else lcm/i for i in self]).view(LatticeIndex)

    def ones(self):
        return np.array([1 if i == 0 else i for i in self]).view(LatticeIndex)
