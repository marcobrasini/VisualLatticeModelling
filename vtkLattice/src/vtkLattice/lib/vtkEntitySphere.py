from vtkmodules.vtkRenderingCore import vtkPolyDataMapper
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourceSphere import vtkSourceSphere


class vtkEntitySphere(vtkEntity):

    def __init__(self):
        self.source = vtkSourceSphere()
        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.SetMapper(self.mapper)

    def center(self):
        return self.source.center()

    def set_center(self, center):
        self.source.set_center(center)
        return self
