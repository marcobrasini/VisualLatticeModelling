import math
from vtkmodules.vtkCommonCore import vtkCommand, vtkMath
from vtkmodules.vtkInteractionWidgets import (
    vtkCompassRepresentation,
    vtkCompassWidget
)

class vtkViewerCamera(vtkCompassWidget):

    def __init__(self, renderer):
        super().__init__()
        self.SetCurrentRenderer(renderer)
        self.compassRepresentation = vtkCompassRepresentation()
        self.compassRepresentation.SetMinimumDistance(0.1)
        self.compassRepresentation.SetMaximumDistance(10)
        self.SetRepresentation(self.compassRepresentation)
        self.AddObserver(
            vtkCommand.WidgetValueChangedEvent,
            vtkViewerCamera.CompassWidgetValueChangedCallback
        )
        self.SetDistance(6)
        self.SetTilt(10)
        self.SetHeading(30)
        self.SetTiltSpeed(5)
        self.SetDistanceSpeed(5)

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