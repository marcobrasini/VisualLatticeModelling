from vtkmodules.vtkRenderingCore import vtkAssembly, vtkRenderer
from ..lib.vtkOutlet import vtkOutlet


class vtkGroup(vtkOutlet, vtkAssembly):

    def render(self, renderer: vtkRenderer):
        renderer.AddActor(self)

    def translate(self, displacement):
        self.SetOrigin(displacement)

    def rotate(self, angle, axis):
        self.RotateWXYZ(angle, *axis)

    def rescale(self, factor):
        self.SetScale(factor)
