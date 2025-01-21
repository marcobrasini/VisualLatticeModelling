from abc import abstractmethod
from .vtkPicker import vtkPicker


class vtkDrawer(vtkPicker):

    def __init__(self, widget):
        super().__init__(widget)
        self.color = (1.0, 0.0, 0.0)
        self.points = []
        self.filter = vtkPicker.localPickFilter

    def pickedEvent(self, picked):
        if self.picking:
            super()._select(picked)
            self.points.append(picked.GetCenter())
            print(self.points)
        else:
            super()._remove(picked)
            self.points.remove(picked.GetCenter())
        self.draw()

    def reset(self):
        self.points = []
        super().reset()

    def clean(self):
        self.points = []
        super().clean()

    def draw(self):
        self.renderer().RemoveActor(self.entity)
        self.entity.set_points(self.points)
        self.entity.render(self.renderer())
