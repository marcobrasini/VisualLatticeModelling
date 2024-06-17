from PyQt5.QtWidgets import QAction
from PyQt5.QtCore import pyqtSignal
from .lib.MyDialog import MyDialogSign
from .QtMenuItem import QtMenuItem


class DialogExit(MyDialogSign):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setWindowTitle('Exit')
        self.setText('Do you want to exit?')


class QtMenuFile(QtMenuItem):

    exitSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        #
        self.addSeparator()
        self.exit = QAction('Exit')
        self.exit.triggered.connect(self.emit_exitSignal)
        self.addAction(self.exit)
        self.setTitle('File')

    def selectValid(self, viewer, lattice):
        self.viewer.validViewer(viewer)
        self.lattice.validLattice(viewer, lattice)

    def emit_exitSignal(self):
        exitDialog = DialogExit()
        if exitDialog.exec():
            self.exitSignal.emit()
