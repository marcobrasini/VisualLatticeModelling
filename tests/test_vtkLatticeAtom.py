import numpy as np
from Lattice import LatticeAtom, LatticeSite
from src.vtkLattice.vtkLatticeAtom import vtkLatticeAtom
from . import render

class Test_vtkLatticeAtom:

    site = LatticeSite([0.2, 0.0, 0.0], basis=2*np.identity(3))
    atom = LatticeAtom('Si', 'Si0', site, np.array([0.7, 0.7, 0.0]))


@render
def test_rendering():
    atom = Test_vtkLatticeAtom.atom
    vtkatom = vtkLatticeAtom(atom)
    vtkatom.source.draw(True, True)
    vtkatom.set_image([[0,0,0], [1,0,0], [0,1,0], [1,1,0]])
    return vtkatom
