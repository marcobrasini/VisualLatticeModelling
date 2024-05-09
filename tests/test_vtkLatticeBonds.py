from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from src.vtkLattice.vtkLatticeBonds import vtkLatticeBonds
from . import Example, render


class Test_vtkLatticeBonds:

    atoms = Example.lattice.atoms
    bonds = Example.lattice.bonds

    vtkatoms = vtkLatticeAtoms(atoms)

    def test__init__(self):
        vtkbonds = vtkLatticeBonds(self.bonds, self.vtkatoms)

    def test_index(self):
        vtkbonds = vtkLatticeBonds(self.bonds, self.vtkatoms)
        for i in range(len(vtkbonds)):
            assert vtkbonds.index(self.bonds[i]) == i


@render
def test_rendering():
    bonds = Test_vtkLatticeBonds.bonds
    vtkatoms = Test_vtkLatticeBonds.vtkatoms
    return vtkatoms, vtkLatticeBonds(bonds, vtkatoms)
