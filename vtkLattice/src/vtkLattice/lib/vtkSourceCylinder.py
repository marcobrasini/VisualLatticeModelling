from vtkmodules.vtkFiltersSources import vtkCylinderSource
from ..lib.vtkSource import vtkSource


class vtkSourceCylinder(vtkSource):

    def __init__(self):
        super().__init__()
        self.source = vtkCylinderSource()
        self.SetInputConnection(self.source.GetOutputPort())

    def radius(self):
        return self.source.GetRadius()

    def length(self):
        return self.source.GetHeight()

    def resolution(self):
        return self.source.GetResolution()

    def set_radius(self, radius):
        self.source.SetRadius(radius)
        return self

    def set_length(self, length):
        self.source.SetHeight(length)
        return self

    def set_resolution(self, resolution):
        self.source.SetResolution(resolution)
        return self