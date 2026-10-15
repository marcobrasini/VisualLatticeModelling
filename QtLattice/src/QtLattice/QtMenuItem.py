from PyQt5.QtWidgets import QMenu
from .QtMenuItemViewer import QtMenuItemViewer
from .QtMenuItemLattice import QtMenuItemLattice
from .QtViewerModel import QtViewerModel


class QtMenuItem(QMenu):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        #
        self.addSeparator()
        self.viewer = QtMenuItemViewer(self)
        self.addAction(self.viewer.header)
        self.addAction(self.viewer.open)
        self.addAction(self.viewer.print)
        self.addAction(self.viewer.close)
        #
        self.addSeparator()
        self.lattice = QtMenuItemLattice(self)
        self.addAction(self.lattice.header)
        self.addAction(self.lattice.open)
        self.addAction(self.lattice.load)
        self.addAction(self.lattice.save)
        self.addAction(self.lattice.close)
        #
        self.aboutToShow.connect(self.selectValid)
        self.viewer.openViewer.connect(self.request_openViewer)
        self.viewer.printViewer.connect(self.request_printViewer)
        self.viewer.closeViewer.connect(self.request_closeViewer)
        self.lattice.openLattice.connect(self.request_openLattice)
        self.lattice.loadLattice.connect(self.request_loadLattice)
        self.lattice.saveLattice.connect(self.request_saveLattice)
        self.lattice.closeLattice.connect(self.request_closeLattice)

    def model(self) -> QtViewerModel:
        return self.parent().model

    def request_openViewer(self, name: str):
        if name:
            self.model().appendViewer(name)
    #
    def request_printViewer(self, files):
        index = self.model().currentIndex()
        if len(index) > 0:
            for file in files:
                self.model().exportViewer(index[0], file)

    def request_closeViewer(self):
        index = self.model().currentIndex()
        if len(index) > 0:
            self.model().removeViewer(index[0])

    def request_openLattice(self, files):
        for file in files:
            index = self.model().viewerCount()
            self.model().appendViewer(f"vtkViewer[{index}]")
            self.model().appendLattice(index, file)

    def request_loadLattice(self, files):
        index = self.model().currentIndex()
        if len(index) > 0:
            for file in files:
                self.model().appendLattice(index[0], file)

    def request_saveLattice(self, files):
        index = self.model().currentIndex()
        if len(index) > 1:
            for file in files:
                self.model().exportLattice(index[0], index[1], file)

    def request_closeLattice(self):
        index = self.model().currentIndex()
        if len(index) > 1:
            self.model().removeLattice(index[0], index[1])

    def selectValid(self):
        index = self.model().currentIndex()
        if len(index) > 1:
            viewer = self.model().currentViewer()
            lattice = self.model().currentLattice()
            self.viewer.validViewer(viewer)
            self.lattice.validLattice(viewer, lattice)
        elif len(index) > 0:
            viewer = self.model().currentViewer()
            self.viewer.validViewer(viewer)
            self.lattice.validLattice(viewer, None)
        else:
            self.viewer.validViewer(None)
            self.lattice.validLattice(None, None)
