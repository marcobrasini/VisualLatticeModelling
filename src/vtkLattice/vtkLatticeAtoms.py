from Lattice import LatticeAtom, LatticeAtoms
from .lib.vtkArray import vtkArray
from .vtkLatticeAtom import vtkLatticeAtom


class vtkLatticeAtoms(vtkArray):

    def __init__(self,
                 atoms: LatticeAtoms
                 ):
        vtkatoms = [vtkLatticeAtom(atom) for atom in atoms]
        super().__init__(vtkatoms)

    def index(self, item):
        if isinstance(item, LatticeAtom):
            return self.atoms().index(item)
        return super().index(item)

    def atoms(self):
        return [vtkatom.atom for vtkatom in self.array]

    def render(self, renderer):
        for atom in self:
            atom.render(renderer)

    def delete(self, renderer):
        for atom in self:
            atom.delete(renderer)

    def translate(self, displacement):
        for atom in self:
            atom.translate(displacement)

    def draw(self, sphere=True, arrow=True, invert=False):
        for atom in self:
            atom.draw(sphere, arrow, invert)

    def visible(self, visibility):
        for entity in self:
            entity.setVisible(visibility)
