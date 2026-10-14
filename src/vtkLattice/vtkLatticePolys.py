from pyLattice import LatticePolys, LatticePoly
from .lib.vtkArray import vtkArray
from .vtkLatticeAtoms import vtkLatticeAtoms
from .vtkLatticePoly import vtkLatticePoly


class vtkLatticePolys(vtkArray):

    def __init__(self,
                 polys: LatticePolys,
                 vtkatoms: vtkLatticeAtoms
                 ):
        vtkpolys = [vtkLatticePoly(poly, vtkatoms) for poly in polys]
        super().__init__(vtkpolys)

    def index(self, item):
        if isinstance(item, LatticePoly):
            return self.polys().index(item)
        return super().index(item)

    def polys(self):
        return [vtkpoly.poly for vtkpoly in self]
