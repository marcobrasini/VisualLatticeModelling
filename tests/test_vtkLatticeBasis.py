from src.vtkLattice.vtkLatticeBasis import vtkLatticeBasis
from . import Example, render


class Test_vtkLatticeBasis:
    pass


@render
def test_rendering():
    basis = Example.lattice().basis
    vtkbasis = vtkLatticeBasis(basis)
    return vtkbasis
