from vtkmodules.vtkRenderingCore import vtkActor, vtkMapper, vtkRenderer
from ..lib.vtkSource import vtkSource
from ..lib.vtkOutlet import vtkOutlet


class vtkEntity(vtkOutlet, vtkActor):

    source: vtkSource
    mapper: vtkMapper

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

    def focusing(self):
        return self.GetProperty().GetEdgeVisibility()

    def set_focusing(self, focus, color=(0., 0., 0.)):
        self.GetProperty().SetEdgeColor(color)
        self.GetProperty().SetEdgeVisibility(focus)

    def visibility(self):
        return self.GetVisibility()

    def set_visibility(self, visibility):
        self.SetVisibility(visibility)

    def set_visible(self, visible):
        if not visible:
            self.visible = self.GetVisibility()
        self.SetVisibility(self.visible and visible)

    def color(self):
        return self.GetProperty().GetColor()

    def set_color(self, color):
        self.GetProperty().SetColor(color)
        return self

    def opacity(self):
        return self.GetProperty().GetOpacity()

    def set_opacity(self, opacity):
        self.GetProperty().SetOpacity(opacity)
        return self

    def linewidth(self):
        return self.GetProperty().GetLineWidth()

    def set_linewidth(self, width):
        self.GetProperty().SetLineWidth(width)
        return self

    # def transparency(self):
    #

    def set_transparency(self, transparency):
        if transparency:
            self.GetProperty().SetRepresentationToWireframe()
        else:
            self.GetProperty().SetRepresentationToSurface()
