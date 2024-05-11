from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePolyline import vtkSourcePolyline


class vtkEntityPolyline(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePolyline()
        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)

    def points(self):
        return self.source.points

    def color(self):
        return self.actor.GetProperty().GetColor()

    def set_points(self, points):
        self.source.set_points(points)
        self.source.set_indices([*(i for i in range(len(points))), 0])
        return self

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self
