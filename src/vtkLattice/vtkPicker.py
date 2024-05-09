from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import vtkPropPicker, vtkAreaPicker
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper2D, vtkActor2D, vtkAssembly
from .lib.vtkSourcePolyline import vtkSourcePolyline


class vtkPickerSingle(vtkPropPicker):
    def __init__(self):
        super().__init__()

    def __call__(self, x0, y0, renderer):
        self.Pick(x0, y0, 0, renderer)
        return self.GetActor()


class vtkPickerRubber(vtkAreaPicker):

    def __init__(self):
        super().__init__()
        self.source = vtkSourcePolyline()
        self.source.set_indices([[0,1,2,3,0]])
        self.mapper = vtkPolyDataMapper2D()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor2D()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetColor((1.0, 0.0, 0.0))

    def __call__(self, x0, y0, x1, y1, renderer):
        self.AreaPick(x0, y0, x1, y1, renderer)
        return self.GetProp3Ds()

    def draw(self, x0, y0, x1, y1):
        self.source.set_points([[x0, y0, 0],
                                [x1, y0, 0],
                                [x1, y1, 0],
                                [x0, y1, 0]])


class vtkPicker(vtkInteractorStyleTrackballCamera):

    def __init__(self):
        super().__init__()
        self.picked = []
        self.picking = False
        self.collect = True
        self.pickerSingle = vtkPickerSingle()
        self.pickerRubber = vtkPickerRubber()
        self.AddObserver("RightButtonPressEvent", self.rightPressed)
        self.AddObserver("RightButtonReleaseEvent", self.rightReleased)
        self.AddObserver("MouseMoveEvent", self.mouseMoved)
        self.AddObserver("KeyPressEvent", self.keyPressed)
        self.AddObserver("KeyReleaseEvent", self.keyRelease)
        self.renderer = self.GetCurrentRenderer

    def keyPressed(self, obj, event):
        if self.GetInteractor().GetShiftKey():
            self.collect = False
        else:
            key = self.GetInteractor().GetKeySym()
            if key == "Delete":
                self.hide()
            if key == "Insert":
                self.show()

    def keyRelease(self, obj, event):
        self.collect = True

    def rightPressed(self, obj, event):
        self.x0, self.y0 = self.GetInteractor().GetEventPosition()
        picked = self.pickerSingle(self.x0, self.y0, self.renderer())
        if picked:
            self.pickedEvent(picked)
            return
        self.picking = True
        self.xmax, self.ymax = self.GetInteractor().GetRenderWindow().GetSize()
        self.renderer().AddActor2D(self.pickerRubber.actor)

    def rightReleased(self, obj, event):
        if self.picking:
            picked = self.pickerRubber(*self.pickedRange(), self.renderer())
            for item in picked:
                if isinstance(item, vtkAssembly):
                    [self.pickedEvent(part) for part in item.GetParts()]
                else:
                    self.pickedEvent(item)
            self.renderer().RemoveActor(self.pickerRubber.actor)
            self.renderer().GetRenderWindow().Render()
            self.pickerRubber.draw(0, 0, 0, 0)
            self.picking = False

    def mouseMoved(self, obj, event):
        if self.picking:
            self.pickerRubber.draw(*self.pickedRange())
            self.renderer().GetRenderWindow().Render()
        self.OnMouseMove()


    def pickedRange(self):
        x0, y0 = self.x0, self.y0
        x1, y1 = self.GetInteractor().GetEventPosition()
        x0, x1 = max(0, min(x0, x1, self.xmax)), min(max(0, x0, x1), self.xmax)
        y0, y1 = max(0, min(y0, y1, self.ymax)), min(max(0, y0, y1), self.ymax)
        return x0, y0, x1, y1


    def pickedEvent(self, picked):
         if self.collect:
             self.__select(picked)
         else:
             self.__remove(picked)

    def __select(self, picked):
        if not picked in self.picked:
            picked.GetProperty().EdgeVisibilityOn()
            self.picked.append(picked)
            self.renderer().GetRenderWindow().Render()

    def __remove(self, picked):
        if picked in self.picked:
            picked.GetProperty().EdgeVisibilityOff()
            self.picked.remove(picked)
            self.renderer().GetRenderWindow().Render()

    def hide(self):
        for item in self.picked:
            item.VisibilityOff()
        self.renderer().GetRenderWindow().Render()

    def show(self):
        for item in self.picked:
            item.VisibilityOn()
        self.renderer().GetRenderWindow().Render()
