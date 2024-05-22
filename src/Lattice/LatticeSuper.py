import numpy as np
from .LatticeIndex import LatticeIndex
from .LatticeBasis import LatticeBasis
from .LatticeAtoms import LatticeAtoms


class LatticeSuper:

    def __init__(self, index):
        self.index = LatticeIndex(index).ones()

    def ncell(self):
        ncell = self.index[0]*self.index[1]*self.index[2]
        return abs(ncell)

    def name(self):
        return "{}x{}x{}".format(*self.index)

    def basis(self, basis):
        super_basis = np.identity(3) * self.index
        return super_basis @ basis

    def sites(self, sites):
        super_sites = sites
        for n, axis in zip(np.abs(self.index), np.identity(3)):
            for i in range(1, n):
                super_sites = np.vstack((super_sites, sites + i*axis))
            sites = super_sites
        return super_sites / np.abs(self.index)

    def atoms(self, atoms):
        super_atoms = atoms
        for n in np.abs(self.index):
            super_atoms = np.tile(super_atoms, n)
        return super_atoms

    def make_name(self, name):
        return name + "_" + self.name()

    def make_basis(self, basis):
        super_basis = self.basis(basis)
        super_basis = LatticeBasis(super_basis)
        super_basis.parameter = basis.parameter
        return super_basis

    def make_atoms(self, atoms, basis):
        super_atoms = self.atoms(atoms.atoms())
        super_sites = self.sites(atoms.sites())
        return LatticeAtoms(basis=basis).make(super_atoms, sites=super_sites)
