from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from src.vtkLattice.vtkLatticeBonds import vtkLatticeBonds
from . import Example, render


class Test_vtkLatticeAtoms:

    atoms = Example.lattice.atoms
    bonds = Example.lattice.bonds

    vtkatoms = vtkLatticeAtoms(atoms)

    def test__init__(self):
        vtkbonds = vtkLatticeBonds(self.bonds, self.vtkatoms)


@render
def test_rendering():
    bonds = Test_vtkLatticeAtoms.bonds
    vtkatoms = Test_vtkLatticeAtoms.vtkatoms
    return vtkatoms, vtkLatticeBonds(bonds, vtkatoms)
