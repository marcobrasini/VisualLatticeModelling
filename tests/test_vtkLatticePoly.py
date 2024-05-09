import numpy as np

from Lattice import LatticePoly, LatticeAtoms, LatticeAtom, LatticeSite
from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from src.vtkLattice.vtkLatticeAtom import vtkLatticeAtom
from src.vtkLattice.vtkLatticePoly import vtkLatticePoly
from . import render


class Test_vtkLatticePoly:

    basis = 4 * np.identity(3)
    atoms = ['O', 'O', 'O', 'O']
    sites = np.array([[0.0, 0.0, 0.0],
                      [0.5, 0.5, 0.0],
                      [0.5, 0.0, 0.5],
                      [0.0, 0.5, 0.5]])
    atoms = LatticeAtoms(basis=basis).make(atoms, sites=sites)
    center = LatticeAtom('Si', site=LatticeSite([0.25, 0.25, 0.25], basis))
    poly = LatticePoly(atoms, center)

    def test__init__(self):
        poly = vtkLatticePoly(self.poly)


@render
def test_rendering():
    atoms = vtkLatticeAtoms(Test_vtkLatticePoly.atoms)
    center = vtkLatticeAtom(Test_vtkLatticePoly.center)
    poly = Test_vtkLatticePoly.poly
    return vtkLatticePoly(poly), atoms, center
