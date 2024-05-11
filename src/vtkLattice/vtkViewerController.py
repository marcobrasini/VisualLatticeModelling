from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from .vtkViewerPicker import vtkViewerPicker


class vtkViewerController(vtkInteractorStyleTrackballCamera):

    def __init__(self):
        super().__init__()
        self.viewerPicker = vtkViewerPicker(self)
        self.picker = self.viewerPicker
        self.AddObserver("RightButtonPressEvent", self.rightPressed)
        self.AddObserver("RightButtonReleaseEvent", self.rightReleased)
        self.AddObserver("MouseMoveEvent", self.mouseMoved)
        self.AddObserver("KeyPressEvent", self.keyPressed)
        self.AddObserver("KeyReleaseEvent", self.keyRelease)

    def keyPressed(self, obj, event):
        if self.GetInteractor().GetShiftKey():
            self.picker.collect = False
        else:
            key = self.GetInteractor().GetKeySym()
            if key == 'Delete':
                self.picker.hide()
            if key == 'Insert':
                self.picker.show()

    def keyRelease(self, obj, event):
        self.picker.collect = True

    def rightPressed(self, obj, event):
        self.picker.rightPressed(obj, event)

    def rightReleased(self, obj, event):
        self.picker.rightReleased(obj, event)

    def mouseMoved(self, obj, event):
        self.picker.mouseMoved(obj, event)
        self.OnMouseMove()
