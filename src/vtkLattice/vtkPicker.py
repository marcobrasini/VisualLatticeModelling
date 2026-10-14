from vtkmodules.vtkRenderingCore import vtkCellPicker
from .lib.vtkImage import vtkImage


class vtkPicker(vtkCellPicker):

    @staticmethod
    def localPickFilter(*actors):
        if actors:
            for image in actors:
                yield image

    @staticmethod
    def totalPickFilter(*actors):
        if actors:
            for image in actors:
                yield image.parent if isinstance(image, vtkImage) else image

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.picking = True
        self.filter = vtkPicker.localPickFilter
        self.picked = []

    def window(self):
        return self.widget.window()

    def renderer(self):
        return self.widget.renderer()

    def interactor(self):
        return self.widget.interactor()

    def pick(self, x0, y0):
        self.Pick(x0, y0, 0, self.renderer())
        return self.GetActor()

    def rightPressed(self, obj, event):
        self.x0, self.y0 = self.interactor().GetEventPosition()
        picked = self.pick(self.x0, self.y0)
        if picked:
            self.pickedEvent(next(self.filter(picked)))
            return picked

    def rightReleased(self, obj, event):
        self.renderer().GetRenderWindow().Render()

    def mouseMoved(self, obj, event):
        pass

    def pickedEvent(self, picked):
         if self.picking:
             self._select(picked)
         else:
             self._remove(picked)

    def _select(self, picked):
        if not picked in self.picked:
            picked.set_focusing(True, self.color)
            self.picked.append(picked)

    def _remove(self, picked):
        if picked in self.picked:
            picked.set_focusing(False, self.color)
            self.picked.remove(picked)

    def hide(self):
        for item in self.picked:
            item.set_visibility(False)
        self.window().Render()

    def show(self):
        for item in self.picked:
            item.set_visibility(True)
        self.window().Render()

    def clean(self):
        to_clean = []
        for item in self.picked:
            if item.visibility():
                item.set_focusing(False)
                to_clean.append(item)
        for item in to_clean:
            self.picked.remove(item)
        self.window().Render()

    def reset(self):
        for item in self.picked:
            item.set_visibility(True)
            item.set_focusing(False)
        self.window().Render()
        self.picked = []
