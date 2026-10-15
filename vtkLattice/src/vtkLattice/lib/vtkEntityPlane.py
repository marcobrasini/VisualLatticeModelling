from vtkmodules.vtkRenderingCore import vtkDataSetMapper
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourcePlane import vtkSourcePlane


DEFAULT_COLOR = (0.5, 0.5, 0.5)


class vtkEntityPlane(vtkEntity):

    def __init__(self):
        self.source = vtkSourcePlane()
        self.mapper = vtkDataSetMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.SetMapper(self.mapper)
        self.set_color(DEFAULT_COLOR)

    def points(self):
        points = [
            self.source.origin(),
            self.source.source.GetPoint1(),
            self.source.source.GetPoint2(),
        ]
        return points

    def set_points(self, points):
        self.source.source.SetOrigin(points[0])
        self.source.source.SetPoint1(points[1])
        self.source.source.SetPoint2(points[2])
        return self
