from src.vtkLattice.vtkLatticeCell import vtkLatticeCell
from . import Example, render


class Test_vtkLatticeCell:
    pass


@render
def test_rendering():
    basis = Example.lattice().basis
    vtkcell = vtkLatticeCell(basis)
    vtkcell.set_color((1.0, 0.0, 0.0))
    vtkcell.set_linewidth(2)
    return vtkcell
