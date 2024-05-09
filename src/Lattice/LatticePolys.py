import numpy as np

from .LatticeArray import LatticeArray
from .LatticeAtoms import LatticeAtoms
from .LatticePoly import LatticePoly


class LatticePolys(LatticeArray):

    def volumes(self):
        return super().get_method('volume')

    def areas(self):
        return super().get_method('area')

    def make(self,
             centers: LatticeAtoms,
             atoms: LatticeAtoms,
             n: int):
        basis = self.basis
        _polys = []
        for center in centers:
            variation = atoms.sites() - center.site
            variation = variation.centered().norm()
            index = np.argsort(variation)[:n]
            _polys.append(LatticePoly(atoms.take(index), center))
        self = np.append(self, _polys).view(LatticePolys)
        self.basis = basis
        return self
