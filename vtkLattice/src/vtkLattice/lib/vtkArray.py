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

    def render(self, renderer: vtkRenderer):
        for entity in self:
            entity.render(renderer)

    def delete(self, renderer: vtkRenderer):
        for entity in self:
            entity.delete(renderer)

    def translate(self, displacement):
        for entity in self:
            entity.translate(displacement)

    def rotate(self, angle, axis):
        for entity in self:
            entity.rotate(angle, axis)

    def rescale(self, factor):
        for entity in self:
            entity.rescale(factor)

    def set_focusing(self, focusing, color=(0., 0., 0.)):
        for entity in self:
            entity.set_focusing(focusing, color)

    def set_visibility(self, visibility):
        for entity in self:
            entity.set_visibility(visibility)

    def set_visible(self, visible):
        for entity in self:
            entity.set_visible(visible)

    def set_opacity(self, opacity):
        for entity in self:
            entity.set_opacity(opacity)

    def set_transparency(self, transparency):
        for entity in self:
            entity.set_transparency(transparency)

    def set_linewidth(self, linewidth):
        for entity in self:
            entity.set_linewidth(linewidth)

    def set_color(self, color):
        for entity in self:
            entity.set_color(color)