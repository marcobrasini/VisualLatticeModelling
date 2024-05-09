import sys
from PyQt5.Qt import QApplication
from PyQt5.QtWidgets import QMainWindow, QFrame, QVBoxLayout
from .vtkViewer import vtkViewer
from .vtkLattice import vtkLattice


def display(lattice: vtkLattice):

    class QtWindow(QMainWindow):

        def __init__(self):
            QMainWindow.__init__(self)
            self.frame = QFrame()
            self.viewer = vtkViewer()
            self.layout = QVBoxLayout()
            self.layout.addWidget(self.viewer)
            self.frame.setLayout(self.layout)
            self.setCentralWidget(self.frame)

    app = QApplication(sys.argv)
    window = QtWindow()
    window.viewer.load_lattice(lattice)
    window.show()
    sys.exit(app.exec_())
