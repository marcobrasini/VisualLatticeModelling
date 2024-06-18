from PyQt5.QtCore import QModelIndex, pyqtSignal
from PyQt5.QtGui import QStandardItemModel
from vtkLattice import vtkLattice, vtkViewer
from .QtViewerItem import QtViewerItem


class QtViewerModel(QStandardItemModel):

    rootSelected = pyqtSignal()
    viewerSelected = pyqtSignal(int)
    viewerInserted = pyqtSignal(int)
    viewerExported = pyqtSignal(int)
    viewerRenamed = pyqtSignal(int)
    viewerRemoved = pyqtSignal(int)
    viewerUpdated = pyqtSignal(int)
    latticeSelected = pyqtSignal(int, int)
    latticeInserted = pyqtSignal(int, int)
    latticeExported = pyqtSignal(int, int)
    latticeRenamed = pyqtSignal(int, int)
    latticeRemoved = pyqtSignal(int, int)
    latticeUpdated = pyqtSignal(int, int)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.current = QModelIndex()
        self.root = self.invisibleRootItem
        self.itemChanged.connect(self.nameChanged)
        self.itemChanged.connect(self.stateChanged)

    # Custom methods
    def setup(self, model):
        self.clear()
        self.setHorizontalHeaderLabels(['QtViewer'])
        for viewer in model:
            viewerItem = QtViewerItem().setVTKViewerItem(viewer)
            self.appendRow(viewerItem)

    def __str__(self, *args):
        report = "QtViewer:\n"
        for i in range(self.viewerCount()):
            viewer = self.viewerItem(i)
            report += f"\t[{i}]:\t{viewer.name()}\n"
            for j in range(self.latticeCount(i)):
                lattice = self.latticeItem(i, j)
                report += f"\t\t[{j}]:\t{lattice.name()}\n"
        return report

    def currentIndex(self):
        if self.current.isValid():
            if self.current.parent().isValid():
                return (self.current.parent().row(), self.current.row(),)
            return (self.current.row(),)
        return ()

    def currentViewer(self):
        index = self.currentIndex()
        if len(index) > 0:
            return self.viewer(index[0])

    def currentLattice(self):
        index = self.currentIndex()
        if len(index) > 1:
            return self.lattice(index[0], index[1])

    def viewerCount(self) -> int:
        return self.rowCount()

    def latticeCount(self, i) -> int:
        return self.viewerItem(i).rowCount()

    def viewerItem(self, i: int) -> QtViewerItem:
        return self.item(i)

    def latticeItem(self, i: int, j: int) -> QtViewerItem:
        return self.item(i).child(j)

    def viewer(self, i: int) -> vtkViewer:
        return self.viewerItem(i).vtk

    def lattice(self, i: int, j: int) -> vtkLattice:
        return self.latticeItem(i, j).vtk

    ###########################################################################
    def selectRoot(self):
        self.current = QModelIndex()
        self.rootSelected.emit()

    # viewer modifiers
    def selectViewer(self, i: int):
        self.current = self.viewerItem(i).index()
        self.viewerSelected.emit(i)

    def appendViewer(self, viewer: vtkViewer | str):
        viewer = QtViewerItem().setVTKViewerItem(viewer)
        self.appendRow(viewer)
        self.viewerInserted.emit(self.viewerCount() - 1)

    def insertViewer(self, i: int, vtkviewer: vtkViewer | str):
        viewer = QtViewerItem().setVTKViewerItem(vtkviewer)
        self.insertRow(i, viewer)
        self.viewerInserted.emit(i)

    def exportViewer(self, i: int, file: str):
        self.viewerExported.emit(i)

    def renameViewer(self, i: int,  name: str):
        if name:
            self.viewerItem(i).setName(name)

    def removeViewer(self, i: int):
        self.removeRow(i)
        self.viewerRemoved.emit(i)
        self.selectRoot()

    ###########################################################################
    # Lattice modifiers
    def selectLattice(self, i: int, j: int):
        self.current = self.latticeItem(i, j).index()
        self.latticeSelected.emit(i, j)

    def appendLattice(self, i: int, lattice: vtkLattice | str):
        lattice = QtViewerItem().setVTKLatticeItem(lattice)
        self.viewerItem(i).appendRow(lattice)
        self.latticeInserted.emit(i, self.latticeCount(i) - 1)

    def insertLattice(self, i: int, j: int, lattice: vtkLattice | str):
        lattice = QtViewerItem().setVTKLatticeItem(lattice)
        self.viewerItem(i).insertRow(j, lattice)
        self.latticeInserted.emit(i, j)

    def exportLattice(self, i: int, j: int, file: str):
        self.latticeExported.emit(i, j)

    def renameLattice(self, i: int, j: int, name: str):
        if name:
            self.latticeItem(i, j).setName(name)

    def removeLattice(self, i: int, j: int):
        self.viewerItem(i).removeRow(j)
        self.latticeRemoved.emit(i, j)
        self.selectViewer(i)

    ###########################################################################
    def nameChanged(self, item: QtViewerItem):
        if item.checkState() == item.visible:
            index = item.index()
            if item.isVTKViewerItem():
                self.viewerRenamed.emit(index.row())
            if item.isVTKLatticeItem():
                self.latticeRenamed.emit(index.parent().row(), index.row())

    def stateChanged(self, item: QtViewerItem):
        if item.isVTKLatticeItem() and item.checkState() != item.visible:
            index = item.index()
            self.lattice(index.parent().row(), index.row()).visible(bool(item.visible))
            self.latticeUpdated.emit(index.parent().row(), index.row())
            item.visible = item.checkState()
