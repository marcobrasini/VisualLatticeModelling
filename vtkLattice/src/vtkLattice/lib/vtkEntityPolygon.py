from vtkmodules.vtkRenderingCore import vtkPolyDataMapper
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePolygon import vtkSourcePolygon


DEFAULT_OPACITY = 0.5
DEFAULT_COLOR = (0.5, 0.5, 0.5)


class vtkEntityPolygon(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePolygon()
        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.SetMapper(self.mapper)
        self.GetProperty().SetEdgeColor((0.5, 0.5, 0.5))
        self.set_color(DEFAULT_COLOR)
        self.set_opacity(DEFAULT_OPACITY)
        self.GetProperty().SetEdgeVisibility(True)

    def points(self):
        return self.source.points

    def set_points(self, points):
        self.source.source.Reset()
        self.source.set_points(points)
        self.source.set_indices([[i for i in range(len(points))]])
        return self
