from vtkmodules.vtkRenderingCore import vtkRenderer
from ..lib.vtkOutlet import vtkOutlet


class vtkArray(vtkOutlet):

    def __init__(self, array):
        super().__init__()
        self.array = array

    def __len__(self):
        return self.array.__len__()

    def __iter__(self):
        return self.array.__iter__()

    def __getitem__(self, item):
        return self.array.__getitem__(item)

    def __contains__(self, item):
        return self.array.__contains__(item)

    def index(self, item):
        return self.array.index(item)

    def actor(self):
        return (entity.actor for entity in self)

    def render(self, renderer: vtkRenderer):
        for actor in self.actor():
            renderer.AddActor(actor)

    def delete(self, renderer: vtkRenderer):
        for actor in self.actor():
            renderer.RemoveActor(actor)

    def translate(self, displacement):
        for actor in self.actor():
            actor.SetPosition(displacement)

    def rotate(self, angle, axis):
        for actor in self.actor():
            actor.RotateWXYZ(angle, *axis)

    def rescale(self, factor):
        for actor in self.actor():
            actor.SetScale(factor)

    def visible(self, visibility):
        for entity in self:
            entity.visible(visibility)
