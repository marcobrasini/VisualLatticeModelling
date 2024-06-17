from vtkmodules.vtkRenderingCore import vtkActor, vtkMapper, vtkRenderer
from ..lib.vtkSource import vtkSource
from ..lib.vtkOutlet import vtkOutlet


class vtkEntity(vtkOutlet):

    source: vtkSource
    mapper: vtkMapper
    actor: vtkActor

    def render(self, renderer: vtkRenderer):
        renderer.AddActor(self.actor)

    def delete(self, renderer: vtkRenderer):
        renderer.RemoveActor(self.actor)

    def translate(self, displacement):
        self.actor.SetPosition(displacement)

    def rotate(self, angle, axis):
        self.actor.RotateWXYZ(angle, *axis)

    def rescale(self, factor):
        self.actor.SetScale(factor)

    def visible(self, visibility):
        if not visibility:
            self.visibility = self.actor.GetVisibility()
        self.actor.SetVisibility(self.visibility and visibility)
