from vtkmodules.vtkRenderingCore import vtkAreaPicker, vtkInteractorStyle
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper2D, vtkActor2D
from .lib.vtkSourcePolyline import vtkSourcePolyline
from .vtkPicker import vtkPicker


class vtkPickerArea(vtkAreaPicker):

    def __init__(self):
        super().__init__()
        self.source = vtkSourcePolyline()
        self.source.set_indices([[0, 1, 2, 3, 0]])
        self.mapper = vtkPolyDataMapper2D()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor2D()
        self.actor.SetMapper(self.mapper)
        self.actor.GetProperty().SetColor((1.0, 0.0, 0.0))

    def __call__(self, x0, y0, x1, y1, renderer):
        self.AreaPick(x0, y0, x1, y1, renderer)
        return self.GetProp3Ds()

    def draw(self, x0, y0, x1, y1):
        self.source.set_points([
            [x0, y0, 0], [x1, y0, 0], [x1, y1, 0], [x0, y1, 0]
        ])


class vtkWidgetPicker(vtkPicker):

    def __init__(self, widget):
        super().__init__(widget)
        self.color = (0., 0., 0.)
        self.selecting = False
        self.areaPicker = vtkPickerArea()
        self.areaPicker.SetRenderer(self.renderer())
        self.pickerFilter = vtkPicker.localPickFilter

    def rightPressed(self, obj, event):
        picked = super().rightPressed(obj, event)
        if picked is None:
            self.selecting = True
            self.xmax, self.ymax = self.window().GetSize()
            self.renderer().AddActor2D(self.areaPicker.actor)

    def rightReleased(self, obj, event):
        if self.selecting:
            picked = self.areaPicker(*self.pickedRange(), self.renderer())
            for item in self.filter(*picked):
                self.pickedEvent(item)
            self.renderer().RemoveActor(self.areaPicker.actor)
            self.areaPicker.draw(0, 0, 0, 0)
            self.selecting = False
        super().rightReleased(obj, event)

    def mouseMoved(self, obj, event):
        if self.selecting:
            self.areaPicker.draw(*self.pickedRange())
            self.window().Render()
        super().mouseMoved(obj, event)

    def pickedRange(self):
        x0, y0 = self.x0, self.y0
        x1, y1 = self.interactor().GetEventPosition()
        x0, x1 = max(0, min(x0, x1, self.xmax)), min(max(0, x0, x1), self.xmax)
        y0, y1 = max(0, min(y0, y1, self.ymax)), min(max(0, y0, y1), self.ymax)
        return x0, y0, x1, y1
