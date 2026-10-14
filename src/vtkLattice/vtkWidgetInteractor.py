from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import vtkInteractorStyle


class vtkWidgetInteractor:

    def __init__(self, widget):
        self.widget = widget
        self.picker = widget.picker
        self.style = vtkInteractorStyleTrackballCamera()
        self.style.AddObserver("RightButtonPressEvent", self.rightPressed)
        self.style.AddObserver("RightButtonReleaseEvent", self.rightReleased)
        self.style.AddObserver("MouseMoveEvent", self.mouseMoved)
        self.style.AddObserver("CharEvent", self.OnChar)
        self.style.AddObserver("KeyPressEvent", self.keyPressed)
        self.style.AddObserver("KeyReleaseEvent", self.keyRelease)

    def GetInteractor(self):
        return self.style.GetInteractor()

    def window(self):
        return self.widget.window()

    def renderer(self):
        return self.widget.renderer()

    def interactor(self):
        return self.widget.interactor()

    def OnChar(self, obj, event):
        key = self.GetInteractor().GetKeyCode()
        if key in ['p', '3']:
            return
        vtkInteractorStyle.OnChar(self.style)

    def keyPressed(self, obj, event):
        if self.GetInteractor().GetShiftKey():
            self.picker.picking = False
        else:
            key = self.GetInteractor().GetKeySym()
            if key == 'Delete':
                self.picker.hide()
            if key == 'Insert':
                self.picker.show()
            if key == '1':
                self.draw_polyline()
            if key == '2':
                self.draw_polygon()
            if key == '3':
                self.draw_poly()
            if key == 'Escape':
                self.escape()
            if key == 'p':
                self.widget.print()
            if key == 'v':
                for lattice in self.widget.viewer.lattice:
                    lattice.atoms.draw(False, True, True)
            if key == 'b':
                for lattice in self.widget.viewer.lattice:
                    lattice.atoms.draw(True, False, False)

    def keyRelease(self, obj, event):
        self.picker.picking = True

    def rightPressed(self, obj, event):
        self.picker.rightPressed(obj, event)

    def rightReleased(self, obj, event):
        self.picker.rightReleased(obj, event)

    def mouseMoved(self, obj, event):
        self.picker.mouseMoved(obj, event)
        self.style.OnMouseMove()

    def escape(self):
        self.picker.clean()
        self.picker = self.widget.picker

    def draw_polyline(self):
        self.picker.clean()
        self.widget.drawer.drawing_polyline()
        self.picker = self.widget.drawer.drawer

    def draw_polygon(self):
        self.picker.clean()
        self.widget.drawer.drawing_polygon()
        self.picker = self.widget.drawer.drawer

    def draw_poly(self):
        self.picker.clean()
        self.widget.drawer.drawing_poly()
        self.picker = self.widget.drawer.drawer

    def pick_open(self, picker):
        self.picker.clean()
        self.picker = picker