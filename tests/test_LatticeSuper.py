import numpy as np
from src.Lattice.LatticeSuper import LatticeSuper
from src.Lattice.LatticeBasis import LatticeBasis
from src.Lattice.LatticeAtoms import LatticeAtoms
from . import Example


class Test_LatticeSuper:

    index = [1, 2,-2]
    ncell = 4
    name = "test"
    supername = "test_1x2x-2"
    basis = Example.basis
    superbasis = np.copy(basis)
    superbasis[0] *= index[0]
    superbasis[1] *= index[1]
    superbasis[2] *= index[2]

    sites = Example.sites
    supersites = sites
    supersites = np.vstack((supersites, supersites + np.array([0, 1, 0])))
    supersites = np.vstack((supersites, supersites + np.array([0, 0, 1])))
    supersites[:, 0] /= index[0]
    supersites[:, 1] /= index[1]
    supersites[:, 2] /= index[2]
    atoms = Example.atoms
    superatoms = np.hstack((atoms, atoms, atoms, atoms))

    def test__init__(self):
        supercell = LatticeSuper(self.index)
        assert np.array_equal(supercell.index, self.index)

    def test__init__zeros(self):
        supercell = LatticeSuper([0, 2, 0])
        assert np.array_equal(supercell.index, [1, 2, 1])

    def test_ncell(self):
        supercell = LatticeSuper(self.index)
        assert supercell.ncell() == self.ncell

    def test_name(self):
        supercell = LatticeSuper(self.index)
        assert supercell.name() == "1x2x-2"

    def test_make_name(self):
        supercell = LatticeSuper(self.index)
        supername = supercell.make_name(self.name)
        assert supername == self.supername

    def test_basis(self):
        supercell = LatticeSuper(self.index)
        superbasis = supercell.basis(self.basis)
        assert np.array_equal(superbasis[0], self.superbasis[0])
        assert np.array_equal(superbasis[1], self.superbasis[1])
        assert np.array_equal(superbasis[2], self.superbasis[2])

    def test_make_basis(self):
        basis = LatticeBasis(self.basis, 2)
        supercell = LatticeSuper(self.index)
        superbasis = supercell.make_basis(basis)
        assert isinstance(superbasis, LatticeBasis)
        assert np.array_equal(superbasis, self.superbasis * 2)
        assert superbasis.parameter == basis.parameter

    def test_sites(self):
        supercell = LatticeSuper(self.index)
        supersites = supercell.sites(self.sites)
        assert supersites.shape == (4 * len(self.sites), 3)
        assert np.all(supersites < 1.0)
        assert np.all(supersites > -1.0)
        assert np.array_equal(supersites, self.supersites)

    def test_atoms(self):
        supercell = LatticeSuper(self.index)
        superatoms = supercell.atoms(self.atoms)
        assert len(superatoms) == 4 * len(self.atoms)
        for at, n in zip(*np.unique(superatoms, return_counts=True)):
            assert n == 4 * len(self.atoms[self.atoms==at])
        assert np.array_equal(superatoms, self.superatoms)

    def test_make_atoms(self):
        atoms = LatticeAtoms(basis=self.basis).make(self.atoms, sites=self.sites)
        supercell = LatticeSuper(self.index)
        superatoms = supercell.make_atoms(atoms, self.superbasis)
        assert isinstance(superatoms, LatticeAtoms)
        assert np.array_equal(superatoms.basis, self.superbasis)
        assert np.array_equal(superatoms.sites(), self.supersites)
        assert np.array_equal(superatoms.atoms(), self.superatoms)
