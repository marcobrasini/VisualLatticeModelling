from PyQt5.QtWidgets import QWidget, QSplitter, QGridLayout
from PyQt5.QtCore import Qt, QObject
from .QtViewerModel import QtViewerModel
from .QtViewerTree import QtViewerTree
from .QtViewerTab import QtViewerTab


class QtViewer(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.viewer = QSplitter(Qt.Horizontal)
        self.model = QtViewerModel(self)
        self.tree = QtViewerTree(self)
        self.tab = QtViewerTab(self)
        self.viewer.addWidget(self.tree)
        self.viewer.addWidget(self.tab)
        self.setLayout(QGridLayout())
        self.layout().addWidget(self.viewer)

        self.model.viewerRemoved.connect(self.removeViewer)
        self.tab.viewerRemoved.connect(self.removeViewer)
        self.model.viewerInserted.connect(self.insertViewer)
        self.tab.viewerInserted.connect(self.insertViewer)
        self.model.latticeInserted.connect(self.insertLattice)
        self.tab.latticeInserted.connect(self.insertLattice)
        self.model.latticeRemoved.connect(self.removeLattice)
        self.tab.latticeRemoved.connect(self.removeLattice)
        self.model.viewerRenamed.connect(self.renameViewer)
        self.tab.viewerRenamed.connect(self.renameViewer)

        self.tree.viewerSelected.connect(self.tab.selectViewer)
        self.tab.viewerSelected.connect(self.tree.selectViewer)

    def insertViewer(self, emitter: QObject, i: int):
        receiver = self.tab if emitter == self.model else self.model
        receiver.insertViewer(emitter.viewer(i), i, callback=False)

    def removeViewer(self, emitter: QObject, i: int):
        receiver = self.tab if emitter == self.model else self.model
        receiver.removeViewer(i, callback=False)

    def renameViewer(self, emitter: QObject, i: int, name: str):
        receiver = self.tab if emitter == self.model else self.model
        receiver.renameViewer(i, name, callback=False)

    def insertLattice(self, emitter: QObject, i: int, j: int):
        receiver = self.tab if emitter == self.model else self.model
        receiver.insertLattice(emitter.lattice(i,j), i, j, callback=False)

    def removeLattice(self, emitter: QObject, i: int, j: int):
        receiver = self.tab if emitter == self.model else self.model
        receiver.removeLattice(i, j, callback=False)

    def setupModel(self, model):
        self.model.setupModel(model)
        self.tree.setModel(self.model)
        self.tab.setModel(self.model)

    def closeEvent(self, event):
        self.tree.closeEvent(event)
        self.tab.closeEvent(event)
        super().closeEvent(event)
