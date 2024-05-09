from Lattice import LatticeBond, LatticeBonds
from .vtkLatticeAtoms import vtkLatticeAtoms
from .vtkLatticeBond import vtkLatticeBond
from .lib.vtkArray import vtkArray


class vtkLatticeBonds(vtkArray):

    def __init__(self,
                 bonds: LatticeBonds,
                 vtkatoms: vtkLatticeAtoms,
                 ):
        vtkbonds = [vtkLatticeBond(bond, vtkatoms) for bond in bonds]
        super().__init__(vtkbonds)

    def index(self, item):
        if isinstance(item, LatticeBond):
            return self.bonds().index(item)
        return super().index(item)

    def bonds(self):
        return [vtkbond.bond for vtkbond in self]

