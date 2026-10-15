from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from . import Example, render


class Test_vtkLatticeAtoms:

    def test__init__(self):
        atoms = Example.lattice().atoms
        vtkatoms = vtkLatticeAtoms(atoms)

    def test_index(self):
        atoms = Example.lattice().atoms
        vtkatoms = vtkLatticeAtoms(atoms)
        for i in range(len(vtkatoms)):
            assert vtkatoms.index(atoms[i]) == i

@render
def test_rendering():
    atoms = Example.lattice().atoms
    return vtkLatticeAtoms(atoms)
