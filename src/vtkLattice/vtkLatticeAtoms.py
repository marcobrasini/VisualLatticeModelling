from Lattice import LatticeAtom, LatticeAtoms
from vtkmodules.vtkRenderingCore import vtkRenderer

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
        return [vtkatom.atom for vtkatom in self]

    def render(self, renderer: vtkRenderer):
        for vtkatom in self:
            vtkatom.render(renderer)
