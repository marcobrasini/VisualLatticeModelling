from PyQt5.QtWidgets import QMenuBar, QMenu
from .QtMenuFile import QtMenuFile


class QtViewerBar(QMenuBar):

    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.file = QtMenuFile()
        self.edit = QMenu('Edit')
        self.draw = QMenu('Draw')
        self.view = QMenu('View')
        self.addMenu(self.file)
        self.addMenu(self.edit)
        self.addMenu(self.draw)
        self.addMenu(self.view)

    def setModel(self, model):
        self.model = model

    def selectItem(self, i: int = None, j: int = None):
        self.viewer = None if i is None else self.model.viewer(i)
        self.lattice = None if j is None else self.model.lattice(i, j)
        self.file.selectValid(self.viewer, self.lattice)
