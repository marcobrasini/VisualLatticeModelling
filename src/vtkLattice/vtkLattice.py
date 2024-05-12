from vtkmodules.vtkRenderingCore import vtkRenderer
from Lattice import Lattice
from .vtkLatticeCell import vtkLatticeCell
from .vtkLatticeBasis import vtkLatticeBasis
from .vtkLatticeAtoms import vtkLatticeAtoms
from .vtkLatticeBonds import vtkLatticeBonds
from .vtkLatticePolys import vtkLatticePolys


class vtkLattice:

    def __init__(self, lattice: Lattice):
        self.cell = vtkLatticeCell(lattice.basis)
        self.basis = vtkLatticeBasis(lattice.basis)
        self.atoms = vtkLatticeAtoms(lattice.atoms)
        self.bonds = vtkLatticeBonds(lattice.bonds, self.atoms)
        self.polys = vtkLatticePolys(lattice.polys, self.atoms)

    def render(self, renderer: vtkRenderer):
        self.cell.render(renderer)
        self.basis.render(renderer)
        self.atoms.render(renderer)
        self.bonds.render(renderer)
        self.polys.render(renderer)

    def translate(self, translation):
        self.cell.translate(translation)
        self.basis.translate(translation)
        self.atoms.translate(translation)
        self.bonds.translate(translation)
        self.polys.translate(translation)

    def rotate(self, rotation, axis):
        self.cell.rotate(rotation, axis)
        self.basis.rotate(rotation, axis)
        self.atoms.rotate(rotation, axis)
        self.bonds.rotate(rotation, axis)
        self.polys.rotate(rotation, axis)

    @classmethod
    def load_poscar(cls, poscar):
        lattice = Lattice.load_poscar(poscar)
        return cls(lattice)
