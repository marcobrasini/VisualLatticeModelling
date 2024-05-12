from .vtkPicker import vtkPicker


class vtkDrawerPicker(vtkPicker):

    draw: None

    def __init__(self, parent):
        super().__init__(parent)
        self.points = []
        self.color = (1.0, 0.0, 0.0)

    def pickedEvent(self, picked):
        if self.collect:
            super()._select(picked)
            self.points.append(picked.GetCenter())
        else:
            super()._remove(picked)
            self.points.remove(picked.GetCenter())
        self.draw(self.points)

    def pickedPoints(self):
        return [picked.GetCenter() for picked in self.picked]

    def reset(self):
        self.points = []
        super().reset()

    def clean(self):
        self.points = []
        super().clean()
