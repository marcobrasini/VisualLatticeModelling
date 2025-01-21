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

    def set_focusing(self, focusing, color = (0., 0., 0.)):
        for entity in self.GetParts():
            entity.GetProperty().SetEdgeColor(color)
            entity.GetProperty().SetEdgeVisibility(focusing)

    def visibility(self):
        return self.GetVisibility()

    def set_visibility(self, visibility):
        self.SetVisibility(visibility)

    def set_visible(self, visible):
        if not visible:
            self.visible = self.GetVisibility()
        self.SetVisibility(self.visible and visible)