from PyQt5.QtWidgets import QMainWindow, QSplitter
from PyQt5.QtCore import Qt, QObject
from .QtViewerModel import QtViewerModel
from .QtViewerTree import QtViewerTree
from .QtViewerMenu import QtViewerMenu
from .QtViewerTab import QtViewerTab


class QtViewer(QMainWindow):

    def __init__(self, parent: QObject = None):
        super().__init__(parent=parent)
        self.viewer = QSplitter(Qt.Horizontal)
        self.model = QtViewerModel()
        self.tree = QtViewerTree(self.model)
        self.menu = QtViewerMenu(self.model)
        self.tab = QtViewerTab(self.model)

        self.setMenuBar(self.menu)
        self.viewer.addWidget(self.tree)
        self.viewer.addWidget(self.tab)
        self.setCentralWidget(self.viewer)
        self.showMaximized()
        # model - tab signals
        self.model.viewerSelected.connect(self.tab.selectViewer)
        self.model.viewerInserted.connect(self.tab.insertViewer)
        self.model.viewerRenamed.connect(self.tab.renameViewer)
        self.model.viewerRemoved.connect(self.tab.removeViewer)
        self.model.latticeSelected.connect(self.tab.selectLattice)
        self.model.latticeInserted.connect(self.tab.insertLattice)
        self.model.latticeRemoved.connect(self.tab.removeLattice)
        self.model.latticeUpdated.connect(self.tab.updateLattice)
        self.tab.viewerSelectRequested.connect(self.model.selectViewer)
        self.tab.viewerInsertRequested.connect(self.model.insertViewer)
        self.tab.viewerRenameRequested.connect(self.model.renameViewer)
        self.tab.viewerRemoveRequested.connect(self.model.removeViewer)
        self.tab.latticeInsertRequested.connect(self.model.insertLattice)
        self.tab.latticeRemoveRequested.connect(self.model.removeLattice)
        #
        self.model.rootSelected.connect(self.tree.selectRoot)
        self.model.viewerSelected.connect(self.tree.selectViewer)
        self.model.latticeSelected.connect(self.tree.selectLattice)
        #
        self.menu.file.exitSignal.connect(self.close)

    def setup(self, model):
        self.model.setup(model)
        self.tree.setup()
        self.menu.setup()
        self.tab.setup()

    def closeEvent(self, event):
        self.tree.closeEvent(event)
        self.menu.closeEvent(event)
        self.tab.closeEvent(event)
        super().closeEvent(event)
