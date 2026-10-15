import math
from vtkmodules.vtkCommonCore import vtkCommand, vtkMath
from vtkmodules.vtkInteractionWidgets import (
    vtkCompassRepresentation,
    vtkCompassWidget
)

class vtkWidgetCamera(vtkCompassWidget):

    def __init__(self, widget, camera: tuple = None):
        camera = camera if camera  else (8, 0, 30)
        super().__init__()
        self.widget = widget
        self.SetCurrentRenderer(self.renderer())
        self.SetInteractor(self.interactor())
        self.compassRepresentation = vtkCompassRepresentation()
        self.compassRepresentation.SetMinimumDistance(0.1)
        self.compassRepresentation.SetMaximumDistance(camera[0])
        self.SetRepresentation(self.compassRepresentation)
        self.AddObserver(
            vtkCommand.WidgetValueChangedEvent,
            vtkWidgetCamera.CompassWidgetValueChangedCallback
        )
        self.SetDistance(camera[0])
        self.SetTilt(camera[1])
        self.SetHeading(camera[2])
        self.SetTiltSpeed(5)
        self.SetDistanceSpeed(1)
        self.EnabledOn()

    def window(self):
        return self.widget.window()

    def renderer(self):
        return self.widget.renderer()

    def interactor(self):
        return self.widget.interactor()

    @staticmethod
    def CompassWidgetValueChangedCallback(widget, event):
        tilt = vtkMath.RadiansFromDegrees(widget.GetTilt())
        heading = vtkMath.RadiansFromDegrees(widget.GetHeading())
        distance = widget.GetDistance()

        camera = widget.GetCurrentRenderer().GetActiveCamera()
        camera.SetPosition(
            1000 * math.cos(heading) * math.cos(tilt),
            1000 * math.sin(heading) * math.cos(tilt),
            1000 * math.sin(tilt),
        )
        camera.SetParallelScale(distance)
        camera.SetFocalPoint(0, 0, 0)
        camera.SetViewUp(0, 0, 1)
        camera.SetClippingRange(0, 2000)

        widget.GetCurrentRenderer().Render()