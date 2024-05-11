from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePolyhedron import vtkSourcePolyhedron


class vtkEntityPolyhedron(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePolyhedron()
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
        return self

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self
