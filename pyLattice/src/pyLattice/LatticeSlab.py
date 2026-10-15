import numpy as np
from .LatticePlane import LatticePlane
from .LatticeSuper import LatticeSuper
from .LatticeBasis import LatticeBasis
from .LatticeAtoms import LatticeAtoms
from .LatticeSites import LatticeSites


class LatticeSlab(LatticeSuper):

    def __init__(self, index, axis):
        self.plane = LatticePlane(index)
        if self.plane.abc[axis] == 0:
            msg_err = f"lattice direction {axis} is an in-plane direction."
            raise (IndexError(msg_err))
        self.axis = axis
        super().__init__(self.plane.ncell())

    def name(self):
        return "({:x},{:x},{:x})".format(*self.plane.hkl)

    def basis(self, basis):
        super_basis = super().basis(basis)
        slab_basis = super_basis - super_basis[self.axis]
        slab_basis[self.axis] = super_basis[self.axis]
        slab_basis[self.plane.abc == 0] = super_basis[self.plane.abc == 0]
        slab_basis = np.roll(slab_basis, 2 - self.axis, axis=0)
        return slab_basis

    def sites(self, sites):
        translation = self.plane.ncell() * np.identity(3)[self.axis]
        super_sites = super().sites(sites) * self.plane.ncell()
        slab_sites = super_sites - translation
        slab_sites[self.plane(super_sites, 0) >= 0] += translation
        slab_sites[self.plane(super_sites, 1) < 0] -= translation
        return slab_sites

    def atoms(self, atoms):
        super_atoms = super().atoms(atoms)
        return super_atoms

    def make_name(self, name):
        return name + "_" + self.name()

    def make_basis(self, basis):
        slab_basis = self.basis(basis)
        slab_basis = LatticeBasis(slab_basis)
        slab_basis.parameter = basis.parameter
        return slab_basis

    def make_atoms(self, atoms, basis):
        slab_atoms = self.atoms(atoms.atoms())
        slab_sites = self.sites(atoms.sites())
        slab_sites = slab_sites @ atoms.basis @ np.linalg.inv(basis)
        slab_sites = LatticeSites(slab_sites, basis=basis).periodic()
        return LatticeAtoms(basis=basis).make(slab_atoms, sites=slab_sites)
