from PyQt5.QtWidgets import QWidget, QSplitter, QGridLayout
from PyQt5.QtCore import Qt
from .QtViewerModel import QtViewerModel
from .QtViewerTree import QtViewerTree
from .QtViewerTab import QtViewerTab


class QtViewer(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.model = QtViewerModel(self)
        self.tree = QtViewerTree(self)
        self.tab = QtViewerTab(self)
        self.viewer = QSplitter(Qt.Horizontal)
        self.viewer.addWidget(self.tree)
        self.viewer.addWidget(self.tab)
        self.setLayout(QGridLayout())
        self.layout().addWidget(self.viewer)


    def setupModel(self, model):
        self.model.setupModel(model)
        self.tab.setModel(self.model)
        self.tree.setModel(self.model)

    def closeEvent(self, event):
        self.tree.closeEvent(event)
        self.tab.closeEvent(event)
        super().closeEvent(event)
