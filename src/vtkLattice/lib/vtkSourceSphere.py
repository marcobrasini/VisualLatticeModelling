from vtkmodules.vtkFiltersSources import vtkSphereSource
from ..lib.vtkSource import vtkSource


class vtkSourceSphere(vtkSource):

    def __init__(self):
        super().__init__()
        self.source = vtkSphereSource()
        self.SetInputConnection(self.source.GetOutputPort())

    def center(self):
        return self.source.GetCenter()

    def radius(self):
        return self.source.GetRadius()

    def resolution(self):
        return self.source.GetPhiResolution(), self.source.GetThetaResolution()

    def set_center(self, center):
        self.source.SetCenter(center)
        return self

    def set_radius(self, radius):
        self.source.SetRadius(radius)
        return self

    def set_resolution(self, *resolution):
        if len(resolution) == 1:
            resolution = (resolution[0], 2*resolution[0])
        self.source.SetPhiResolution(resolution[0])
        self.source.SetThetaResolution(resolution[1])
        return self
