from vtkmodules.vtkRenderingCore import vtkRenderer
from Lattice import Lattice
from .vtkLatticeCell import vtkLatticeCell
from .vtkLatticeBasis import vtkLatticeBasis
from .vtkLatticeAtoms import vtkLatticeAtoms
from .vtkLatticeBonds import vtkLatticeBonds


class vtkLattice:

    def __init__(self, lattice: Lattice):
        self.cell = vtkLatticeCell(lattice.basis)
        self.basis = vtkLatticeBasis(lattice.basis)
        self.atoms = vtkLatticeAtoms(lattice.atoms)
        self.atoms = vtkLatticeBonds(lattice.bonds)

    def render(self, renderer: vtkRenderer):
        pass
