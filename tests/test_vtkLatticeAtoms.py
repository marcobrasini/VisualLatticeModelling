from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from . import Example, render

class Test_vtkLatticeAtoms:

    atoms = Example.lattice.atoms

    def test__init__(self):
        vtkatoms = vtkLatticeAtoms(self.atoms)

    def test_index(self):
        vtkatoms = vtkLatticeAtoms(self.atoms)
        for i in range(len(vtkatoms)):
            assert vtkatoms.index(self.atoms[i]) == i

@render
def test_rendering():
    atoms = Test_vtkLatticeAtoms.atoms
    return vtkLatticeAtoms(atoms)
