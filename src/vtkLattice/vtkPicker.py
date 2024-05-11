from vtkmodules.vtkRenderingCore import vtkPropPicker, vtkInteractorStyle


class vtkPickerProp(vtkPropPicker):
    def __init__(self):
        super().__init__()

    def __call__(self, x0, y0, renderer):
        self.Pick(x0, y0, 0, renderer)
        return self.GetActor()


class vtkPicker:

    def __init__(self,
                 controller: vtkInteractorStyle
                 ):
        self.picked = []
        self.picking = False
        self.collect = True
        self.color = (0., 0., 0.)
        self.propPicker = vtkPickerProp()
        self.controller = controller
        self.interactor = self.controller.GetInteractor
        self.renderer = self.controller.GetCurrentRenderer

    def rightPressed(self, obj, event):
        self.x0, self.y0 = self.interactor().GetEventPosition()
        picked = self.propPicker(self.x0, self.y0, self.renderer())
        if picked:
            self.pickedEvent(picked)
            return picked

    def rightReleased(self, obj, event):
        self.renderer().GetRenderWindow().Render()

    def mouseMoved(self, obj, event):
        pass

    def pickedEvent(self, picked):
         if self.collect:
             self.__select(picked)
         else:
             self.__remove(picked)

    def __select(self, picked):
        if not picked in self.picked:
            picked.GetProperty().EdgeVisibilityOn()
            picked.GetProperty().SetEdgeColor(self.color)
            self.picked.append(picked)

    def __remove(self, picked):
        if picked in self.picked:
            picked.GetProperty().EdgeVisibilityOff()
            self.picked.remove(picked)

    def hide(self):
        for item in self.picked:
            item.VisibilityOff()
        self.renderer().GetRenderWindow().Render()

    def show(self):
        for item in self.picked:
            item.VisibilityOn()
        self.renderer().GetRenderWindow().Render()

    def clean(self):
        to_clean = []
        for item in self.picked:
            if item.GetVisibility():
                item.GetProperty().EdgeVisibilityOff()
                to_clean.append(item)
        for item in to_clean:
            self.picked.remove(item)
        self.renderer().GetRenderWindow().Render()

    def reset(self):
        for item in self.picked:
            item.VisibilityOn()
            item.GetProperty().EdgeVisibilityOff()
        self.renderer().GetRenderWindow().Render()
        self.picked = []
