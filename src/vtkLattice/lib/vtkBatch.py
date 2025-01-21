from vtkmodules.vtkRenderingCore import vtkMapper, vtkRenderer
from ..lib.vtkOutlet import vtkOutlet
from ..lib.vtkSource import vtkSource


class vtkBatch(vtkOutlet, list):

    source: vtkSource
    images: list

    def render(self, renderer: vtkRenderer):
        for image in self:
            renderer.AddActor(image)

    def delete(self, renderer: vtkRenderer):
        for image in self:
            renderer.RemoveActor(image)

    def translate(self, displacement):
        for image in self:
            image.translate(displacement)

    def rotate(self, angle, axis):
        for image in self:
            image.rotate(angle, axis)

    def rescale(self, factor):
        for image in self:
            image.rescale(factor)

    def set_focusing(self, focusing, color=(0., 0., 0.)):
        for image in self:
            image.set_focusing(focusing, color)

    def visibility(self):
        visibility = [image.visibility() for image in self]
        return any(visibility)

    def set_visibility(self, visibility):
        for image in self:
            image.set_visibility(visibility)

    def set_visible(self, visible):
        for image in self:
            image.set_visible(visible)

    def set_linewidth(self, linewidth):
        for image in self:
            image.set_linewidth(linewidth)

    def set_color(self, color):
        for image in self:
            image.set_color(color)
        return self

    def set_opacity(self, opacity):
        for image in self:
            image.set_opacity(opacity)
        return self

    def set_transparency(self, transparency):
        for image in self:
            image.set_transparency(transparency)

    def set_ambient(self, ambient):
        for image in self:
            image.set_ambient(ambient)

    def set_diffuse(self, diffuse):
        for image in self:
            image.set_diffuse(diffuse)

    def set_specular(self, specular):
        for image in self:
            image.set_specular(specular)

    def set_wireframe(self):
        for image in self:
            image.GetProperty().SetRepresentationToWireframe()

    def set_images(self, images):
        self.clear()
        self.images = []
        for image in images:
            self.add_image(image)
        return self

    def add_image(self, image):
        self.append(self.new_image(image))
        self.images.append(image)

    def new_image(self, image):
        pass
