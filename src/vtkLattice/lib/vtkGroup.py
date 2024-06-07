from vtkmodules.vtkRenderingCore import vtkAssembly, vtkRenderer
from ..lib.vtkOutlet import vtkOutlet


class vtkGroup(vtkOutlet, vtkAssembly):

    def render(self, renderer: vtkRenderer):
        renderer.AddActor(self)

    def delete(self, renderer: vtkRenderer):
        renderer.RemoveActor(self)

    def translate(self, displacement):
        self.SetPosition(displacement)

    def rotate(self, angle, axis):
        self.RotateWXYZ(angle, *axis)

    def rescale(self, factor):
        self.SetScale(factor)

    def visible(self, visibility):
        if not visibility:
            self.visibility = self.GetVisibility()
        self.SetVisibility(self.visibility and visibility)
