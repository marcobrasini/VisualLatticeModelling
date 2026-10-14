from vtkmodules.vtkRenderingCore import vtkRenderer
from pyLattice import Lattice
from .vtkLatticeCell import vtkLatticeCell
from .vtkLatticeBasis import vtkLatticeBasis
from .vtkLatticeAtoms import vtkLatticeAtoms
from .vtkLatticeBonds import vtkLatticeBonds
from .vtkLatticePolys import vtkLatticePolys


class vtkLattice:

    def __init__(self, lattice: Lattice):
        self.lattice = lattice
        self.name = lattice.name
        self.cell = vtkLatticeCell(lattice.basis)
        self.basis = vtkLatticeBasis(lattice.basis)
        self.atoms = vtkLatticeAtoms(lattice.atoms)
        self.bonds = vtkLatticeBonds(lattice.bonds, self.atoms)
        self.polys = vtkLatticePolys(lattice.polys, self.atoms)

    def parent(self):
        return self._parent

    def setParent(self, parent):
        self._parent = parent

    def render(self, renderer: vtkRenderer):
        self.cell.render(renderer)
        self.basis.render(renderer)
        self.atoms.render(renderer)
        self.bonds.render(renderer)
        self.polys.render(renderer)

    def delete(self, renderer: vtkRenderer):
        self.cell.delete(renderer)
        self.basis.delete(renderer)
        self.atoms.delete(renderer)
        self.bonds.delete(renderer)
        self.polys.delete(renderer)

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

    def visible(self, visibility):
        self.cell.visible(visibility)
        self.basis.visible(visibility)
        self.atoms.visible(visibility)
        self.bonds.visible(visibility)
        self.polys.visible(visibility)

    @classmethod
    def load_poscar(cls, poscar):
        lattice = Lattice.load_poscar(poscar)
        return cls(lattice)

    def save_poscar(self, poscar):
        return self.lattice.save_poscar(poscar)
