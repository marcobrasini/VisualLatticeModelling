from vtkmodules.vtkCommonCore import vtkMath
from vtkmodules.vtkFiltersSources import vtkArrowSource
from ..lib.vtkSource import vtkSource


class vtkSourceArrow(vtkSource):

    def __init__(self):
        super().__init__()
        self.source = vtkArrowSource()
        self.SetInputConnection(self.source.GetOutputPort())

    def set_vector(self, vector):
        self.orientate(vector, axis=0)
        self.rescale((vtkMath.Norm(vector), 1.0, 1.0))
        return self

    def set_origin(self, origin):
        self.translate(origin)
        return self

    def set_ratio(self, ratio):
        self.source.SetTipLength(ratio)
        return self

    def set_radius(self, *radius):
        if len(radius) == 1:
            radius = (radius[0], 2*radius[0])
        self.source.SetShaftRadius(radius[0])
        self.source.SetTipRadius(radius[1])
        return self

    def set_resolution(self, *resolution):
        if len(resolution) == 1:
            resolution = (resolution[0], resolution[0])
        self.source.SetShaftResolution(resolution[0])
        self.source.SetTipResolution(resolution[1])
        return self

    def vector(self):
        length = self.length()
        matrix = self.transformation.orientation
        return [length * matrix.GetElement(0, i) for i in range(3)]

    def origin(self):
        return self.transformation.translation

    def length(self):
        return self.transformation.scale[0]

    def ratio(self):
        return self.source.GetTipLength()

    def radius(self):
        return self.source.GetShaftRadius(), self.source.GetTipRadius()

    def resolution(self):
        return self.source.GetShaftResolution(), self.source.GetTipResolution()
