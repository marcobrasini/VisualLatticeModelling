from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from src.vtkLattice.vtkLatticeBonds import vtkLatticeBonds
from . import Example, render


class Test_vtkLatticeBonds:

    def test__init__(self):
        bonds = Example.lattice().bonds
        vtkatoms = vtkLatticeAtoms(Example.lattice().atoms)
        vtkbonds = vtkLatticeBonds(bonds, vtkatoms)

    def test_index(self):
        bonds = Example.lattice().bonds
        vtkatoms = vtkLatticeAtoms(Example.lattice().atoms)
        vtkbonds = vtkLatticeBonds(bonds, vtkatoms)
        for i in range(len(vtkbonds)):
            assert vtkbonds.index(bonds[i]) == i


@render
def test_rendering():
    bonds = Example.lattice().bonds
    vtkatoms = vtkLatticeAtoms(Example.lattice().atoms)
    return vtkatoms, vtkLatticeBonds(bonds, vtkatoms)
