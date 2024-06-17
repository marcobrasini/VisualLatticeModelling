from PyQt5.QtWidgets import QTreeView, QAbstractItemView
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QModelIndex
from PyQt5.QtGui import QMouseEvent
from .QtMenuItem import QtMenuItem


class QtViewerTree(QTreeView):

    rootSelected = pyqtSignal()
    latticeSelected = pyqtSignal(int, int)
    viewerSelected = pyqtSignal(int)
    viewerRenamed = pyqtSignal(str)
    viewerPrinted = pyqtSignal(int)

    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        index = self.indexAt(event.pos())
        if index.isValid():
            if self.model().itemFromIndex(index).isVTKViewerItem():
                self.viewerSelected.emit(index.row())
            if self.model().itemFromIndex(index).isVTKLatticeItem():
                self.latticeSelected.emit(index.parent().row(), index.row())
        else:
            self.clearSelection()
            self.rootSelected.emit()

    def selectViewer(self, i: int, callback: bool = True):
        if self.selectedViewer().row() != i:
            self.setCurrentIndex(self.model().createIndex(i, 0))

    def contextMenu(self, point: QPoint):
        menu = QtMenuItem(self)
        menu.viewer.openViewer.connect(self.openViewer)
        menu.viewer.closeViewer.connect(self.closeViewer)
        menu.viewer.printViewer.connect(self.printViewer)
        menu.viewer.renameViewer.connect(self.renameViewer)
        menu.lattice.openLattice.connect(self.openLattice)
        menu.lattice.loadLattice.connect(self.loadLattice)
        menu.lattice.saveLattice.connect(self.saveLattice)
        menu.lattice.renameLattice.connect(self.renameLattice)
        menu.lattice.removeLattice.connect(self.removeLattice)
        menu.selectItem(self.viewer(), self.lattice())
        menu.exec(self.viewport().mapToGlobal(point))

    def selected(self):
        index = self.selectedIndexes()
        if index:
            return index[0]
        return QModelIndex()

    def selectedViewer(self):
        index = self.selected()
        if index.isValid():
            if self.model().itemFromIndex(index).isVTKViewerItem():
                return index
            if self.model().itemFromIndex(index).isVTKLatticeItem():
                return index.parent()
        return QModelIndex()

    def selectedLattice(self):
        index = self.selected()
        if index.isValid():
            if self.model().itemFromIndex(index).isVTKLatticeItem():
                return index
        return QModelIndex()

    def viewer(self):
        index = self.selectedViewer()
        if index.isValid():
            return self.model().viewer(index.row())

    def lattice(self):
        index = self.selectedLattice()
        if index.isValid():
            return self.model().lattice(index.parent().row(), index.row())

    def isViewer(self):
        return self.selectedViewer().isValid()

    def isLattice(self):
        return self.selectedLattice().isValid()

    def openViewer(self, name: str):
        self.model().appendViewer(name)

    def renameViewer(self):
        index = self.selectedViewer()
        if index.isValid():
            self.edit(index)

    def printViewer(self):
        index = self.selectedViewer()
        if index.isValid():
            self.viewerPrinted.emit(index.row())

    def closeViewer(self):
        index = self.selectedViewer()
        if index.isValid():
            self.model().removeViewer(index.row())

    def openLattice(self, files: list):
        for file in files:
            self.openViewer(f"vtkViewer[{self.model().viewerCount()}]")
            self.model().appendLattice(file, self.model().viewerCount() - 1)

    def loadLattice(self, files: list):
        for file in files:
            self.model().appendLattice(file, self.selectedViewer().row())

    def saveLattice(self, files: list):
        index = self.selectedLattice()
        if index.isValid():
            for file in files:
                lattice = self.model().lattice(index.parent().row(), index.row())
                lattice.save_poscar(file)

    def renameLattice(self):
        index = self.selectedLattice()
        if index.isValid():
            self.edit(index)

    def removeLattice(self):
        index = self.selectedLattice()
        if index.isValid():
            self.model().removeLattice(index.parent().row(), index.row())
