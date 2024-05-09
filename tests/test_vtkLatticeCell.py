from src.vtkLattice.vtkLatticeCell import vtkLatticeCell
from . import Example, render


class Test_vtkLatticeCell:

    basis = Example.lattice.basis


@render
def test_rendering():
    basis = Test_vtkLatticeCell.basis
    vtkcell = vtkLatticeCell(basis)
    vtkcell.set_color((1.0, 0.0, 0.0))
    vtkcell.set_width(2)
    return vtkcell
