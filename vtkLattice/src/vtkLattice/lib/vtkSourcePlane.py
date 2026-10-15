from vtkmodules.vtkFiltersSources import vtkPlaneSource
from ..lib.vtkSource import vtkSource


class vtkSourcePlane(vtkSource):

    def __init__(self):
        super().__init__()
        self.source = vtkPlaneSource()
        self.source.SetXResolution(100)
        self.source.SetYResolution(100)
        self.SetInputConnection(self.source.GetOutputPort())

    def origin(self):
        return self.source.GetOrigin()

    def set_origin(self, origin):
        vectors = self.vectors()
        self.source.SetOrigin(origin)
        self.set_vectors(*vectors)
        return self

    def center(self):
        vectors = self.vectors()
        return self.source.GetCenter()
        # return [0.5*(a + b) for a, b in zip(*vectors)]

    def set_center(self, center):
        # vectors = self.vectors()
        self.source.SetCenter(center)
        # self.set_vectors(*vectors)

    def normal(self):
        return self.source.GetNormal()

    def set_normal(self, normal):
        self.source.SetNormal(normal)
        return self

    def vectors(self):
        origin = self.source.GetOrigin()
        a = [a1 - a0 for a1, a0 in zip(self.source.GetPoint1(), origin)]
        b = [a2 - a0 for a2, a0 in zip(self.source.GetPoint2(), origin)]
        return a, b

    def set_vectors(self, a, b):
        a = [a1+a0 for a1, a0 in zip(a, self.origin())]
        b = [b1+b0 for b1, b0 in zip(b, self.origin())]
        self.source.SetPoint1(a)
        self.source.SetPoint2(b)
        return self
