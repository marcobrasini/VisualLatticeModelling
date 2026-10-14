import numpy as np
from pyLattice import LatticeSite, LatticeAtom, LatticeBond
from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from src.vtkLattice.vtkLatticeBond import vtkLatticeBond
from . import render


class Test_vtkLatticeBond:

    basis = 4 * np.identity(3)
    site1 = LatticeSite([0.1, 0.1, 0.0], basis=basis)
    atom1 = LatticeAtom('Si', 'Si0', site1)
    site2 = LatticeSite([0.8, 0.0, 0.0], basis=basis)
    atom2 = LatticeAtom('O', 'O-', site2)
    bond = LatticeBond(atom1, atom2)

    vtkatoms = vtkLatticeAtoms([atom1, atom2])

    def test_vtk_lattice_bond(self):
        vtkbond = vtkLatticeBond(self.bond, self.vtkatoms)


@render
def test_rendering():
    bond = Test_vtkLatticeBond.bond
    vtkatoms = Test_vtkLatticeBond.vtkatoms
    vtkbonds = vtkLatticeBond(bond, vtkatoms, [[0, 0, 0], [1, 0, 0]])
    vtkbonds.draw(True, True)
    return vtkbonds, vtkatoms