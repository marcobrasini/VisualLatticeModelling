from vtkmodules.vtkRenderingCore import vtkDataSetMapper, vtkActor
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePolyline import vtkSourcePolyline


class vtkEntityPolyline(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePolyline()
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetEdgeColor((0.5, 0.5, 0.5))

    def points(self):
        return self.source.points

    def color(self):
        return self.actor.GetProperty().GetColor()

    def set_points(self, points):
        self.source.set_points(points)
        self.source.set_indices([[i for i in range(len(points))]])
        return self

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self
