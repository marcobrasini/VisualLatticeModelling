from src.vtkLattice.vtkPicker import vtkPicker


class vtkDrawerPicker(vtkPicker):

    draw: None

    def __init__(self, parent):
        super().__init__(parent)
        self.color = (1.0, 0.0, 0.0)

    def pickedEvent(self, picked):
        super().pickedEvent(picked)
        self.draw(self.pickedPoints())
        # TODO: Separate the vtkLatticeAtom images into different actor for drawing.

    def pickedPoints(self):
        return [picked.GetCenter() for picked in self.picked]
