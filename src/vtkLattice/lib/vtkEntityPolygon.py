from vtkmodules.vtkRenderingCore import vtkDataSetMapper, vtkActor
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePolygon import vtkSourcePolygon


DEFAULT_OPACITY = 0.5
DEFAULT_COLOR = (0.5, 0.5, 0.5)


class vtkEntityPolygon(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePolygon()
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetEdgeColor((0.5, 0.5, 0.5))
        self.set_color(DEFAULT_COLOR)
        self.set_opacity(DEFAULT_OPACITY)

    def points(self):
        return self.source.points

    def color(self):
        return self.actor.GetProperty().GetColor()

    def set_points(self, points):
        self.source.source.Reset()
        self.source.set_points(points)
        self.source.set_indices([[i for i in range(len(points))]])
        return self

    def set_opacity(self, opacity):
        self.actor.GetProperty().SetOpacity(opacity)
        return self

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self
