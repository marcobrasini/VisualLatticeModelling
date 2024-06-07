import numpy as np
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from .vtkWidgetPicker import vtkWidgetPicker
from .vtkDrawerPicker import vtkDrawerPicker
from .vtkDrawer import vtkDrawer


class vtkWidgetController(vtkInteractorStyleTrackballCamera):

    def __init__(self, viewer):
        super().__init__()
        self.viewer = viewer
        self.viewerPicker = vtkWidgetPicker(self)
        self.drawerPicker = vtkDrawerPicker(self)
        self.drawer = vtkDrawer(self)
        self.picker = self.viewerPicker
        self.AddObserver("RightButtonPressEvent", self.rightPressed)
        self.AddObserver("RightButtonReleaseEvent", self.rightReleased)
        self.AddObserver("MouseMoveEvent", self.mouseMoved)
        self.AddObserver("CharEvent", self.OnChar)
        self.AddObserver("KeyPressEvent", self.keyPressed)
        self.AddObserver("KeyReleaseEvent", self.keyRelease)

    def OnChar(self, obj, event):
        key = self.GetInteractor().GetKeyCode()
        if key in ['p', '3']:
            return
        super(vtkInteractorStyleTrackballCamera, obj).OnChar()

    def keyPressed(self, obj, event):
        if self.GetInteractor().GetShiftKey():
            self.picker.collect = False
        else:
            key = self.GetInteractor().GetKeySym()
            if key == 'Delete':
                self.picker.hide()
            if key == 'Insert':
                self.picker.show()
            if key == '1':
                self.viewerPicker.clean()
                self.drawerPicker.reset()
                self.drawerPicker.draw = self.drawer.draw_polyline
                self.drawer.init_polyline()
                self.picker = self.drawerPicker
            if key == '2':
                self.viewerPicker.clean()
                self.drawerPicker.reset()
                self.drawerPicker.draw = self.drawer.draw_polygon
                self.drawer.init_polygon()
                self.picker = self.drawerPicker
            if key == '3':
                self.viewerPicker.clean()
                self.drawerPicker.reset()
                self.drawerPicker.draw = self.drawer.draw_poly
                self.drawer.init_poly()
                self.picker = self.drawerPicker
            if key == 'Escape':
                self.picker.clean()
                self.picker = self.viewerPicker
            if key == 'p':
                self.viewer.printer.print(self.viewer.name)
            if key == 'v':
                self.viewer.lattice[0].atoms.draw(False, True, True)
            if key == 'b':
                self.viewer.lattice[0].atoms.draw(True, False, False)

    def keyRelease(self, obj, event):
        self.picker.collect = True

    def rightPressed(self, obj, event):
        self.picker.rightPressed(obj, event)

    def rightReleased(self, obj, event):
        self.picker.rightReleased(obj, event)

    def mouseMoved(self, obj, event):
        self.picker.mouseMoved(obj, event)
        self.OnMouseMove()
