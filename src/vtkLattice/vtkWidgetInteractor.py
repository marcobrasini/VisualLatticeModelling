from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera


class vtkWidgetInteractor(vtkInteractorStyleTrackballCamera):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.picker = self.widget.picker
        self.AddObserver("RightButtonPressEvent", self.rightPressed)
        self.AddObserver("RightButtonReleaseEvent", self.rightReleased)
        self.AddObserver("MouseMoveEvent", self.mouseMoved)
        self.AddObserver("CharEvent", self.OnChar)
        self.AddObserver("KeyPressEvent", self.keyPressed)
        self.AddObserver("KeyReleaseEvent", self.keyRelease)

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
        super(vtkInteractorStyleTrackballCamera, obj).OnChar()

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
        self.OnMouseMove()

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
