from vtkmodules.vtkRenderingCore import vtkDataSetMapper, vtkActor
from Lattice import LatticePoly
from .vtkLatticeAtoms import vtkLatticeAtoms
from .lib.vtkSourcePolyhedron import vtkSourcePolyhedron
from .lib.vtkEntity import vtkEntity


DEFAULT_OPACITY = 0.5


class vtkLatticePoly(vtkEntity):

    def __init__(self,
                 poly: LatticePoly,
                 vtkAtoms: vtkLatticeAtoms
                 ):
        self.poly = poly
        self.center = vtkAtoms[vtkAtoms.index(poly.center)]
        self.source = vtkSourcePolyhedron()
        self.source.set_points(self.poly.points())
        self.source.set_indices(self.poly.simplices())
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
        self.set_color(self.center.color())
        self.set_opacity(DEFAULT_OPACITY)

    def color(self):
        return self.actor.GetProperty().GetColor()

    def width(self):
        return self.actor.GetProperty().GetLineWidth()

    def opacity(self):
        return self.actor.GetProperty().GetOpacity()

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self

    def set_width(self, width):
        self.actor.GetProperty().SetLineWidth(width)
        return self

    def set_opacity(self, opacity):
        self.actor.GetProperty().SetOpacity(opacity)
        return self