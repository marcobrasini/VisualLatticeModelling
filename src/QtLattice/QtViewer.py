from PyQt5.QtWidgets import QMainWindow, QSplitter
from PyQt5.QtCore import Qt, QObject
from .QtViewerModel import QtViewerModel
from .QtViewerTree import QtViewerTree
from .QtViewerTab import QtViewerTab
from .QtViewerBar import QtViewerBar


class QtViewer(QMainWindow):

    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.viewer = QSplitter(Qt.Horizontal)
        self.model = QtViewerModel(self)
        self.tree = QtViewerTree(self)
        self.tab = QtViewerTab(self)
        self.bar = QtViewerBar(self)

        self.setMenuBar(self.bar)
        self.viewer.addWidget(self.tree)
        self.viewer.addWidget(self.tab)
        self.setCentralWidget(self.viewer)
        self.showMaximized()
        # model - tab signals
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
        # tree - tab signals
        self.tree.latticeSelected.connect(self.tab.selectLattice)
        self.tree.viewerSelected.connect(self.tab.selectViewer)
        self.tab.viewerSelected.connect(self.tree.selectViewer)
        # tree - bar signals
        self.tree.rootSelected.connect(self.bar.selectItem)
        self.tree.viewerSelected.connect(self.bar.selectItem)
        self.tree.latticeSelected.connect(self.bar.selectItem)
        self.bar.file.viewer.openViewer.connect(self.tree.openViewer)
        self.bar.file.viewer.openViewer.connect(self.tree.openViewer)
        self.bar.file.viewer.closeViewer.connect(self.tree.closeViewer)
        self.bar.file.viewer.printViewer.connect(self.tree.printViewer)
        self.bar.file.viewer.renameViewer.connect(self.tree.renameViewer)
        self.bar.file.lattice.openLattice.connect(self.tree.openLattice)
        self.bar.file.lattice.loadLattice.connect(self.tree.loadLattice)
        self.bar.file.lattice.saveLattice.connect(self.tree.saveLattice)
        self.bar.file.lattice.renameLattice.connect(self.tree.renameLattice)
        self.bar.file.lattice.removeLattice.connect(self.tree.removeLattice)
        self.bar.file.exitSignal.connect(self.close)

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

    def selectViewer(self, emitter:QObject, i: int):
        receiver = self.tab if emitter == self.tree else self.tree
        receiver.selectViewer(i, callback=False)

    def setupModel(self, model):
        self.model.setupModel(model)
        self.tree.setModel(self.model)
        self.bar.setModel(self.model)
        self.tab.setModel(self.model)

    def closeEvent(self, event):
        self.tree.closeEvent(event)
        self.tab.closeEvent(event)
        self.bar.closeEvent(event)
        super().closeEvent(event)
