from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourceSphere import vtkSourceSphere


class vtkEntitySphere(vtkEntity):

    def __init__(self):
        self.source = vtkSourceSphere()
        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)

    def center(self):
        return self.source.center()

    def color(self):
        return self.actor.GetProperty().GetColor()

    def set_center(self, center):
        self.source.set_center(center)
        return self

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self
