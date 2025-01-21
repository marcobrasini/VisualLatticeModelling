import sys
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QMainWindow, QFrame, QVBoxLayout
from .vtkViewer import vtkViewer
from .vtkWidget import vtkWidget


def display(name: str = "", vtklattices: list = []):
    class QtWindow(QMainWindow):

        def __init__(self):
            QMainWindow.__init__(self)
            self.frame = QFrame()
            self.widget = vtkWidget(vtkViewer(name))
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
    window.viewer.name = name
    window.show()
    app.exec()
    app.exit()
