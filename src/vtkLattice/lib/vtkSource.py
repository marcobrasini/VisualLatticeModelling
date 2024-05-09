from vtkmodules.vtkFiltersGeneral import vtkTransformFilter
from ..lib.vtkTransformation import vtkTransformation


class vtkSource(vtkTransformFilter):

    def __init__(self):
        super().__init__()
        self.transformation = vtkTransformation()
        self.SetTransform(self.transformation())

    def translate(self, displacement):
        self.transformation.translation = displacement
        self.SetTransform(self.transformation())

    def orientate(self, direction, axis):
        orientation = vtkTransformation.make_orientation(direction, axis)
        self.transformation.orientation = orientation
        self.SetTransform(self.transformation())

    def rescale(self, factor):
        scale = [factor]*3 if isinstance(factor, float) else factor
        self.transformation.scale = scale
        self.SetTransform(self.transformation())
