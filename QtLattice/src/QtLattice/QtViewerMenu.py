from PyQt5.QtWidgets import QMenuBar
from .QtViewerModel import QtViewerModel
from .QtMenuItem import QtMenuItem
from .QtMenuFile import QtMenuFile
from .QtMenuEdit import QtMenuEdit
from .QtMenuDraw import QtMenuDraw
from .QtMenuView import QtMenuView


class QtViewerMenu(QMenuBar):

    def __init__(self, model: QtViewerModel, parent = None):
        super().__init__(parent=parent)
        self.model = model
        self.item = QtMenuItem(self)
        self.file = QtMenuFile(self)
        self.edit = QtMenuEdit(self)
        self.draw = QtMenuDraw(self)
        self.view = QtMenuView(self)
        self.addMenu(self.file)
        self.addMenu(self.edit)
        self.addMenu(self.draw)
        self.addMenu(self.view)

    def setup(self):
        pass

