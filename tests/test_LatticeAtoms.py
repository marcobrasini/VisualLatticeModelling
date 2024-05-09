import numpy as np
from copy import deepcopy

from src.Lattice.LatticeAtoms import LatticeAtoms
from src.Lattice.LatticeAtom import LatticeAtom
from src.Lattice.LatticeSite import LatticeSite
from . import Example


class Test_LatticeAtoms:

    basis = Example.basis
    sites = Example.sites
    atoms = Example.atoms
    names = Example.names
    count = Example.count
    vars = Example.vars
    #
    latticeSites = [
        LatticeSite(site, basis=Example.basis) for site in Example.sites
    ]
    latticeAtoms = [
        LatticeAtom(*args) for args in zip(atoms, names, sites, vars)
    ]

    def test__init__(self):
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        for i, atom in enumerate(atoms):
            assert atom == self.latticeAtoms[i]

    def test__getitem__(self):
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        for i in range(len(atoms)):
            assert atoms[i] == self.latticeAtoms[i]

    def test__getitem__atom(self):
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        for at, n in atoms.count().items():
            assert len(atoms[at]) == n

    def test_count(self):
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        assert atoms.count() == self.count

    def test_atoms(self):
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        assert np.array_equal(atoms.atoms(), self.atoms)

    def test_names(self):
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        assert np.array_equal(atoms.names(), self.names)

    def test_sites(self):
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        assert np.array_equal(atoms.sites().basis, self.basis)
        assert np.array_equal(atoms.sites(), self.sites)

    def test_vars(self):
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        assert np.array_equal(atoms.vars(), self.vars)

    def test_set_atoms(self):
        new_atoms = np.array(['']*len(self.atoms))
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        atoms = atoms.set_atoms(new_atoms)
        assert np.array_equal(atoms.atoms(), new_atoms)

    def test_set_names(self):
        new_names = np.array(['_']*len(self.names))
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        atoms = atoms.set_names(new_names)
        assert np.array_equal(atoms.names(), new_names)

    def test_set_sites(self):
        new_sites = np.array([[1., 1., 1.]]*len(self.sites))
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        atoms = atoms.set_sites(new_sites)
        assert np.array_equal(atoms.sites(), new_sites)

    def test_set_vars(self):
        new_vars = np.array([[0., 0., 0.]]*len(self.vars))
        atoms = LatticeAtoms(deepcopy(self.latticeAtoms), basis=self.basis)
        atoms = atoms.set_vars(new_vars)
        assert np.array_equal(atoms.vars(), new_vars)

    def test_make_atom(self):
        atoms = LatticeAtoms(basis=self.basis)
        atoms = atoms.make(self.atoms)
        for i, atom in enumerate(atoms):
            assert atom == LatticeAtom(self.atoms[i])

    def test_make_names(self):
        atoms = LatticeAtoms(basis=self.basis)
        atoms = atoms.make(self.atoms, names=self.names)
        for i, atom in enumerate(atoms):
            assert atom == LatticeAtom(self.atoms[i], self.names[i])

    def test_make_sites(self):
        atoms = LatticeAtoms(basis=self.basis)
        atoms = atoms.make(self.atoms, sites=self.sites)
        for i, atom in enumerate(atoms):
            assert atom == LatticeAtom(self.atoms[i], site=self.latticeSites[i])

    def test_make_vars(self):
        atoms = LatticeAtoms(basis=self.basis)
        atoms = atoms.make(self.atoms, vars=self.vars)
        for i, atom in enumerate(atoms):
            assert atom == LatticeAtom(self.atoms[i], var=self.vars[i])

    def test_make(self):
        atoms = LatticeAtoms(basis=self.basis)
        atoms = atoms.make(self.atoms, self.names, self.sites, self.vars)
        for i, atom in enumerate(atoms):
            self.latticeAtoms[i].site.basis = self.basis
            assert atom == self.latticeAtoms[i]
