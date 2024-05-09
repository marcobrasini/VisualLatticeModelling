from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from src.vtkLattice.vtkLatticePolys import vtkLatticePolys
from . import Example, render


class Test_vtkLatticePolys:

    atoms = Example.lattice.atoms
    polys = Example.lattice.polys

    vtkatoms = vtkLatticeAtoms(atoms)

    def test__init__(self):
        vtkpolys = vtkLatticePolys(self.polys, self.vtkatoms)

    def test_index(self):
        vtkpolys = vtkLatticePolys(self.polys, self.vtkatoms)
        for i in range(len(vtkpolys)):
            assert vtkpolys.index(self.polys[i]) == i

@render
def test_rendering():
    polys = Test_vtkLatticePolys.polys
    vtkatoms = Test_vtkLatticePolys.vtkatoms
    return vtkatoms, vtkLatticePolys(polys, vtkatoms)
