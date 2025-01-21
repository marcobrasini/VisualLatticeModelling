from src.vtkLattice.vtkLatticeAtoms import vtkLatticeAtoms
from src.vtkLattice.vtkLatticePolys import vtkLatticePolys
from . import Example, render


class Test_vtkLatticePolys:

    def test__init__(self):
        polys = Example.lattice().polys
        vtkatoms = vtkLatticeAtoms(Example.lattice().atoms)
        vtkpolys = vtkLatticePolys(polys, vtkatoms)

    def test_index(self):
        polys = Example.lattice().polys
        vtkatoms = vtkLatticeAtoms(Example.lattice().atoms)
        vtkpolys = vtkLatticePolys(polys, vtkatoms)
        for i in range(len(vtkpolys)):
            assert vtkpolys.index(polys[i]) == i


@render
def test_rendering():
    polys = Example.lattice().polys
    vtkatoms = vtkLatticeAtoms(Example.lattice().atoms)
    return vtkatoms, vtkLatticePolys(polys, vtkatoms)
