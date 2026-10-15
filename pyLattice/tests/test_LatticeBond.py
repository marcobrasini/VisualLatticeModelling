import numpy as np
from src.pyLattice.LatticeBond import LatticeBond
from src.pyLattice.LatticeSite import LatticeSite
from src.pyLattice.LatticeAtom import LatticeAtom
from . import Example


class Test_LatticeBond:

    basis = 2*np.identity(3)
    site1 = LatticeSite([0.1, 0.0, 0.0], basis=basis)
    atom1 = LatticeAtom('Si', site=site1)
    site2 = LatticeSite([0.9, 0.0, 0.0], basis=basis)
    atom2 = LatticeAtom('O', site=site2)

    def test__init__(self):
        bond = LatticeBond(self.atom1, self.atom2)
        assert bond.atom1 == self.atom1
        assert bond.atom2 == self.atom2

    def test_vector(self):
        bond = LatticeBond(self.atom1, self.atom2)
        assert isinstance(bond.vector(), LatticeSite)
        assert np.allclose(bond.vector(), np.array([-0.2, 0.0, 0.0]))

    def test_center(self):
        bond = LatticeBond(self.atom1, self.atom2)
        assert isinstance(bond.center(), LatticeSite)
        assert np.allclose(bond.center(), np.array([ 0.0, 0.0, 0.0]))

    def test_versor(self):
        bond = LatticeBond(self.atom1, self.atom2)
        assert not isinstance(bond.versor(), LatticeSite)
        assert np.allclose(bond.versor(), np.array([-1.0, 0.0, 0.0]))

    def test_length(self):
        bond = LatticeBond(self.atom1, self.atom2)
        assert np.isclose(bond.length(), 0.4)

    def test_image(self):
        bond = LatticeBond(self.atom1, self.atom2)
        assert np.array_equal(bond.image(), [-1, 0, 0])
