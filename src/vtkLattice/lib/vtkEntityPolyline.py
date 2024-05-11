from vtkmodules.vtkRenderingCore import vtkDataSetMapper, vtkActor
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePolyline import vtkSourcePolyline


DEFAULT_COLOR = (0.5, 0.5, 0.5)


class vtkEntityPolyline(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePolyline()
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
        self.set_color(DEFAULT_COLOR)

    def points(self):
        return self.source.points

    def color(self):
        return self.actor.GetProperty().GetColor()

    def set_points(self, points):
        self.source.source.Reset()
        self.source.set_points(points)
        self.source.set_indices([[i for i in range(len(points))]])
        return self

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self
