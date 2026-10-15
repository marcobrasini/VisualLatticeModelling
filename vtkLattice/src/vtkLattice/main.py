import sys
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QMainWindow, QFrame, QVBoxLayout
from .vtkViewer import vtkViewer
from .vtkWidget import vtkWidget
from .vtkLattice import vtkLattice


def display(name: str = "", vtklattices: list = [], camera: tuple = (), print=False):

    class QtWindow(QMainWindow):

        def __init__(self):
            QMainWindow.__init__(self)
            self.frame = QFrame()
            self.widget = vtkWidget(vtkViewer(name), camera=camera)
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.widget)
            self.frame.setLayout(self.layout)
            self.setCentralWidget(self.frame)

        def closeEvent(self, event):
            self.widget.close()
            super().closeEvent(event)

    app = QApplication(sys.argv)
    window = QtWindow()
    for lattice in vtklattices:
        window.widget.appendLattice(lattice)
    if camera:
        window.widget.camera.SetDistance(camera[0])
        window.widget.camera.SetTilt(camera[1])
        window.widget.camera.SetHeading(camera[2])
    window.show()
    if print:
        window.widget.print()
        window.close()
        return
    else:
        app.exec()
        app.exit()

