from vtkmodules.vtkRenderingCore import vtkDataSetMapper
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePolyline import vtkSourcePolyline


DEFAULT_COLOR = (0.5, 0.5, 0.5)


class vtkEntityPolyline(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePolyline()
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.SetMapper(self.mapper)
        self.set_color(DEFAULT_COLOR)

    def points(self):
        return self.source.points

    def set_points(self, points):
        self.source.source.Reset()
        self.source.set_points(points)
        self.source.set_indices([[i for i in range(len(points))]])
        return self
