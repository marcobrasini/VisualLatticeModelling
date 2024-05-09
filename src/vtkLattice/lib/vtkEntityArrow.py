from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor
from ..lib.vtkEntity import vtkEntity
from ..lib.vtkSourceArrow import vtkSourceArrow


class vtkEntityArrow(vtkEntity):

    def __init__(self):
        self.source = vtkSourceArrow()
        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)

    def vector(self):
        return self.source.vector()

    def origin(self):
        return self.source.origin()

    def length(self):
        return self.source.length()

    def color(self):
        return self.actor.GetProperty().GetColor()

    def set_vector(self, vector):
        self.source.set_vector(vector)
        return self

    def set_origin(self, origin):
        self.source.set_origin(origin)
        return self

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self
