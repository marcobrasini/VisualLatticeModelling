import scipy as sp
from vtkmodules.vtkFiltersModeling import vtkLinearSubdivisionFilter
from vtkmodules.vtkRenderingCore import vtkDataSetMapper, vtkActor
from pyLattice import LatticePoly
from .lib.vtkBatch import vtkBatch
from .lib.vtkImage import vtkImage
from .lib.vtkSourcePolyhedron import vtkSourcePolyhedron
from .lib.vtkSourcePolygon import vtkSourcePolygon
from .vtkLatticeAtoms import vtkLatticeAtoms


DEFAULT_OPACITY = 0.5


class vtkLatticePoly(vtkBatch):

    def __init__(self,
                 poly: LatticePoly,
                 vtkAtoms: vtkLatticeAtoms,
                 images: list = [[0, 0, 0]]
                 ):
        self.poly = poly
        self.atoms = [vtkAtoms[vtkAtoms.index(atom)] for atom in poly.others]
        self.center = vtkAtoms[vtkAtoms.index(poly.center)]
        try:
            self.source = vtkSourcePolyhedron()
            self.source.set_points(self.poly.points().cartesian())
            self.source.set_indices(self.poly.simplices())
        except sp.spatial._qhull.QhullError:
            self.source = vtkSourcePolygon()
            self.source.set_points(self.poly.points().cartesian())
            self.source.set_indices([[0,1,2, 3]])
        self.color = self.center.color
        self.set_images(images)
        self.set_opacity(DEFAULT_OPACITY)

    def new_image(self, image):
        image = (self.poly.center.site + image).cartesian()
        mapper = vtkDataSetMapper()
        mapper.SetInputConnection(self.source.GetOutputPort())
        return vtkImage(self, mapper, image).set_color(self.color)

    def set_focusing(self, focusing, color=(0., 0., 0.)):
        super().set_focusing(focusing, color)
        super().set_linewidth(3 if focusing else 1)
