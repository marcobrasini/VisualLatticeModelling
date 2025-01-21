import numpy as np
import scipy as sp

from src.Lattice.LatticeSite import LatticeSite
from src.Lattice.LatticeAtom import LatticeAtom
from src.Lattice.LatticeAtoms import LatticeAtoms
from src.Lattice.LatticePoly import LatticePoly
from . import Example


class Test_LatticePoly:

    basis = 2 * np.identity(3)
    atoms = ['O', 'O', 'O', 'O']
    sites = np.array([[0.0, 0.0, 0.0],
                      [0.5, 0.5, 0.0],
                      [0.5, 0.0, 0.5],
                      [0.0, 0.5, 0.5]])
    others = LatticeAtoms(basis=basis).make(atoms, sites=sites)
    center = LatticeAtom('Si', site=LatticeSite([0.25, 0.25, 0.25], basis))

    def test__init__(self):
        poly = LatticePoly(self.others, self.center)
        assert poly.center == self.center
        for i, atom in enumerate(poly.others):
            assert atom == self.others[i]

    def test__init__default(self):
        poly = LatticePoly(self.others)
        assert np.array_equal(poly.center, np.zeros(3))
        for i, atom in enumerate(poly.others):
            assert atom == self.others[i]

    def test_hull(self):
        poly = LatticePoly(self.others, self.center)
        assert isinstance(poly.hull(), sp.spatial.ConvexHull)

    def test_volume(self):
        poly = LatticePoly(self.others, self.center)
        assert np.isclose(poly.volume(), 1/3)

    def test_area(self):
        poly = LatticePoly(self.others, self.center)
        assert np.isclose(poly.area(), 2*np.sqrt(3))
