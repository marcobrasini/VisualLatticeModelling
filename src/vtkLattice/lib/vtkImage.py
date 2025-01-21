from vtkmodules.vtkRenderingCore import vtkActor, vtkRenderer, vtkMapper
from ..lib.vtkOutlet import vtkOutlet


class vtkImage(vtkOutlet, vtkActor):

    mapper: vtkMapper
    position: list

    def __init__(self, parent, mapper, position):
        super().__init__()
        self.visible = True
        self.parent = parent
        self.mapper = mapper
        self.position = position
        self.SetMapper(self.mapper)
        self.SetPosition(position)

    def render(self, renderer: vtkRenderer):
        renderer.AddActor(self)

    def delete(self, renderer: vtkRenderer):
        renderer.RemoveActor(self)

    def translate(self, displacement):
        self.SetPosition(self.position + displacement)

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

    def diffuse(self):
        return self.GetProperty().GetDiffuse()

    def set_diffuse(self, diffuse):
        return self.GetProperty().SetDiffuse(diffuse)

    def specular(self):
        return self.GetProperty().GetSpecular()

    def set_specular(self, specular):
        return self.GetProperty().SetSpecular(specular)

    def ambient(self):
        return self.GetProperty().GetAmbient()

    def set_ambient(self, ambient):
        return self.GetProperty().SetAmbient(ambient)

    def linewidth(self):
        return self.GetProperty().GetLineWidth()

    def set_linewidth(self, width):
        self.GetProperty().SetLineWidth(width)
        return self

    def set_transparency(self, transparency):
        if transparency:
            self.GetProperty().SetRepresentationToWireframe()
            self.set_focusing(True)
        else:
            self.GetProperty().SetRepresentationToSurface()
            self.set_focusing(False)
