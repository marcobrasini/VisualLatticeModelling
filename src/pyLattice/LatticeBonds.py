import numpy as np

from .LatticeBond import LatticeBond
from .LatticeAtoms import LatticeAtoms
from .LatticeArray import LatticeArray


class LatticeBonds(LatticeArray):

    def atoms1(self):
        atoms1 = super().get_attribute('atom1')
        return LatticeAtoms(atoms1, basis=self.basis)

    def atoms2(self):
        atoms2 = super().get_attribute('atom2')
        return LatticeAtoms(atoms2, basis=self.basis)

    def vectors(self):
        vectors = self.atoms2().sites() - self.atoms1().sites()
        return vectors.centered()

    def centers(self):
        atoms1 = self.atoms1()
        vectors = self.vectors()
        return vectors * 0.5 + atoms1.sites()

    def lengths(self):
        vectors = self.vectors().cartesian()
        return np.linalg.norm(vectors, axis=1)

    def versors(self):
        vectors = self.vectors().cartesian()
        return (vectors.T/self.lengths()).T

    def make(self,
             atoms1: LatticeAtoms,
             atoms2: LatticeAtoms,
             r: float):
        basis = self.basis
        _bonds = []
        for atom1 in atoms1:
            variation = atoms2.sites() - atom1.site
            variation = variation.centered().norm()
            for atom2 in atoms2[variation <= r]:
                _bonds.append(LatticeBond(atom1, atom2))
        self = np.append(self, _bonds).view(LatticeBonds)
        self.basis = basis
        return self
