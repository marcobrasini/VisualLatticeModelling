from src.vtkLattice.vtkLatticeBasis import vtkLatticeBasis
from . import Example, render


class Test_vtkLatticeBasis:

    basis = Example.lattice.basis


@render
def test_rendering():
    basis = Test_vtkLatticeBasis.basis
    vtkbasis = vtkLatticeBasis(basis)
    return vtkbasis
