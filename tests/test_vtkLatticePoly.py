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

    vtkatoms = vtkLatticeAtoms([*atoms, center])

    def test__init__(self):
        poly = vtkLatticePoly(self.poly, self.vtkatoms)


@render
def test_rendering():
    vtkatoms = Test_vtkLatticePoly.vtkatoms
    center = vtkLatticeAtom(Test_vtkLatticePoly.center)
    poly = vtkLatticePoly(Test_vtkLatticePoly.poly, vtkatoms)
    return poly, vtkatoms, center
