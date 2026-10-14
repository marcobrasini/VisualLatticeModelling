from copy import deepcopy

import numpy as np

from .LatticeArray import LatticeArray
from .LatticeAtoms import LatticeAtoms
from .LatticePoly import LatticePoly


class LatticePolys(LatticeArray):

    def copy(self):
        return deepcopy(self)

    def centers(self):
        return LatticeAtoms(super().get_attribute('center'), basis=self.basis)

    def others(self):
        return super().get_attribute('others')

    def atoms(self):
        return super().get_method('atoms')

    def volumes(self):
        return super().get_method('volume')

    def areas(self):
        return super().get_method('area')

    def make(self,
             centers: LatticeAtoms,
             others: LatticeAtoms,
             n: int):
        basis = self.basis
        _polys = []
        for center in centers:
            variation = others.sites() - center.site
            variation = variation.centered().norm()
            index = np.argsort(variation)[:n]
            _polys.append(LatticePoly(others.take(index), center))
        self = np.append(self, _polys).view(LatticePolys)
        self.basis = basis
        return self
