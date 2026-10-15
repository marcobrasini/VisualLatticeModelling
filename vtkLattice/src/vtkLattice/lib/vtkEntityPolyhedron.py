from vtkmodules.vtkFiltersModeling import vtkLinearSubdivisionFilter
from vtkmodules.vtkRenderingCore import vtkDataSetMapper
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePolyhedron import vtkSourcePolyhedron


DEFAULT_OPACITY = 0.5
DEFAULT_COLOR = (0.5, 0.5, 0.5)


class vtkEntityPolyhedron(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePolyhedron()
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.SetMapper(self.mapper)
        self.GetProperty().SetEdgeColor((0.5, 0.5, 0.5))
        self.set_color(DEFAULT_COLOR)
        self.set_opacity(DEFAULT_OPACITY)

    def points(self):
        return self.source.points

    def set_points(self, points):
        self.source.source.Reset()
        self.source.set_points(points)
        self.source.set_convex()
        return self
