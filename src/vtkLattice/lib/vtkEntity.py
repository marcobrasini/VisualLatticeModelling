from vtkmodules.vtkRenderingCore import vtkActor, vtkMapper, vtkRenderer
from ..lib.vtkSource import vtkSource
from ..lib.vtkOutlet import vtkOutlet


class vtkEntity(vtkOutlet):

    source: vtkSource
    mapper: vtkMapper
    actor: vtkActor

    def render(self, renderer: vtkRenderer):
        renderer.AddActor(self.actor)

    def translate(self, displacement):
        self.actor.SetOrigin(displacement)

    def rotate(self, angle, axis):
        self.actor.RotateWXYZ(angle, *axis)

    def rescale(self, factor):
        self.actor.SetScale(factor)
