import sys
from vtkLattice import vtkLattice
from PyQt5.Qt import QApplication, Qt
from PyQt5.QtWidgets import QMainWindow, QSplitter, QVBoxLayout
# from .QtMenu import QtMenu
from .QtViewer import QtViewer


class QtMain(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.viewer = QtViewer()
        self.viewer.setupModel([])
        self.setCentralWidget(self.viewer)
        self.showMaximized()

    def closeEvent(self, event):
        self.viewer.closeEvent(event)
        super().closeEvent(event)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QtMain()
    main.show()
    sys.exit(app.exec_())
