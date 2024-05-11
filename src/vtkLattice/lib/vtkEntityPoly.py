import numpy as np
from vtkmodules.vtkRenderingCore import vtkDataSetMapper, vtkActor, vtkRenderer
from ..lib.vtkEntityPolyline import vtkEntityPolyline
from ..lib.vtkEntityPolygon import vtkEntityPolygon
from ..lib.vtkEntityPolyhedron import vtkEntityPolyhedron
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSource import vtkSource


DEFAULT_OPACITY = 0.5
DEFAULT_COLOR = (0.5, 0.5, 0.5)


class vtkEntityPoly(vtkEntity):

    def __init__(self):
        super().__init__()
        self.source = vtkSource()
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
        self.set_color(DEFAULT_COLOR)
        self.set_opacity(DEFAULT_OPACITY)

    def render(self, renderer: vtkRenderer):
        if self.rank:
            super().render(renderer)

    def set_points(self, points):
        self.points = np.array(points)
        self.rank = np.linalg.matrix_rank(self.points - self.points[0])
        if self.rank == 1:
            self.source = vtkEntityPolyline().set_points(self.points).source
            self.mapper.SetInputConnection(self.source.GetOutputPort())
        elif self.rank == 2:
            self.source = vtkEntityPolygon().set_points(self.points).source
            self.mapper.SetInputConnection(self.source.GetOutputPort())
        elif self.rank == 3:
            self.source = vtkEntityPolyhedron().set_points(self.points).source
            self.mapper.SetInputConnection(self.source.GetOutputPort())
        return self

    def set_opacity(self, opacity):
        self.actor.GetProperty().SetOpacity(opacity)
        return self

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self
