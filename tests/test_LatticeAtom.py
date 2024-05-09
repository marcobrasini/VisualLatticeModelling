import numpy as np
from src.Lattice.LatticeAtom import LatticeAtom
from src.Lattice.LatticeSite import LatticeSite
from . import Example

class Test_LatticeAtom:

    basis = Example.basis
    atom = 'Si'
    name = 'Si0'
    site = LatticeSite([0.5, 0.5, 0.5], basis)
    var = np.array([0.1, 0.1, 0.1])

    def test__init__(self):
        atom = LatticeAtom(self.atom, self.name, self.site, self.var)
        assert atom.atom == self.atom
        assert atom.name == self.name
        assert atom.site == self.site
        assert np.array_equal(atom.var, self.var)

    def test__init__default(self):
        atom = LatticeAtom()
        assert atom.atom == ""
        assert atom.name == ""
        assert atom.site == LatticeSite()
        assert np.array_equal(atom.var, np.zeros(3))

    def test__init__default_atom(self):
        atom = LatticeAtom(self.atom)
        assert atom.atom == self.atom
        assert atom.name == self.atom
        assert atom.site == LatticeSite()
        assert np.array_equal(atom.var, np.zeros(3))

    def test__init__default_name(self):
        atom = LatticeAtom(self.atom, name=self.name)
        assert atom.atom == self.atom
        assert atom.name == self.name
        assert atom.site == LatticeSite()
        assert np.array_equal(atom.var, np.zeros(3))

    def test__init__default_site(self):
        atom = LatticeAtom(self.atom, site=self.site)
        assert atom.atom == self.atom
        assert atom.name == self.atom
        assert atom.site == self.site
        assert np.array_equal(atom.var, np.zeros(3))

    def test__init__default_var(self):
        atom = LatticeAtom(self.atom, var=self.var)
        assert atom.atom == self.atom
        assert atom.name == self.atom
        assert atom.site == LatticeSite()
        assert np.array_equal(atom.var, self.var)

    def test__eq__true(self):
        atom1 = LatticeAtom(self.atom, self.name, self.site, self.var)
        atom2 = LatticeAtom(self.atom, self.name, self.site, self.var)
        assert atom1 == atom2

    def test__eq__false_atom(self):
        atom1 = LatticeAtom(self.atom, self.name, self.site, self.var)
        atom2 = LatticeAtom("", self.name, self.site, self.var)
        assert not atom1 == atom2

    def test__eq__false_name(self):
        atom1 = LatticeAtom(self.atom, self.name, self.site, self.var)
        atom2 = LatticeAtom(self.atom, "", self.site, self.var)
        assert not atom1 == atom2

    def test__eq__false_site(self):
        atom1 = LatticeAtom(self.atom, self.name, self.site, self.var)
        atom2 = LatticeAtom(self.atom, self.name, np.zeros(3), self.var)
        assert not atom1 == atom2

    def test__eq__false_var(self):
        atom1 = LatticeAtom(self.atom, self.name, self.site, self.var)
        atom2 = LatticeAtom(self.atom, self.name, self.site, np.zeros(3))
        assert not atom1 == atom2
