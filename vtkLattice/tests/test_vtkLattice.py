from src.vtkLattice.vtkLattice import vtkLattice
from . import Example, render


class Test_vtkLattice:

    lattice = Example.lattice()

    def test__init__(self):
        vtklattice = vtkLattice(self.lattice)


@render
def test_rendering():
    vtklattice = vtkLattice(Test_vtkLattice.lattice)
    return vtklattice
