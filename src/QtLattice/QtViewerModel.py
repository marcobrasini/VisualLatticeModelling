from PyQt5.QtCore import QModelIndex, QObject, pyqtSignal
from PyQt5.QtGui import QStandardItemModel
from vtkLattice import vtkLattice, vtkViewer
from .QtViewerItem import QtViewerItem


class QtViewerModel(QStandardItemModel):

    viewerRenamed = pyqtSignal(QObject, int, str)
    viewerRemoved = pyqtSignal(QObject, int)
    viewerInserted = pyqtSignal(QObject, int)
    latticeRemoved = pyqtSignal(QObject, int, int)
    latticeInserted = pyqtSignal(QObject, int, int)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.root = self.invisibleRootItem
        self.setHorizontalHeaderLabels(['QtViewer'])
        self.itemChanged.connect(self.nameChanged)

    # Custom methods
    def setupModel(self, viewerList):
        for viewer in viewerList:
            viewerItem = QtViewerItem().setVTKViewerItem(viewer)
            self.root().appendRow(viewerItem)

    def printModel(self, *args):
        report = "QtViewer:\n"
        for i in range(self.viewerCount()):
            viewer = self.viewerItem(i)
            report += f"\t[{i}]:\t{viewer.name()}\n"
            for j in range(self.latticeCount(i)):
                lattice = self.latticeItem(i, j)
                report += f"\t\t[{j}]:\t{lattice.name()}\n"
        print(report)

    def viewerCount(self):
        return self.rowCount()

    def latticeCount(self, i):
        return self.viewerItem(i).rowCount()

    def viewerItem(self, i: int) -> QtViewerItem:
        return self.item(i)

    def latticeItem(self, i: int, j: int) -> QModelIndex:
        return self.item(i).child(j)

    def viewer(self, i: int) -> QModelIndex:
        return self.viewerItem(i).vtk

    def lattice(self, i: int, j: int) -> QModelIndex:
        return self.latticeItem(i, j).vtk

    def appendViewer(self, callback: bool = True):
        viewer = QtViewerItem().setVTKViewerItem()
        self.appendRow(viewer)
        if callback:
            self.viewerInserted.emit(self, self.viewerCount())

    def insertViewer(self, vtkviewer: vtkViewer, i: int, callback: bool = True):
        viewer = QtViewerItem().setVTKViewerItem(vtkviewer)
        self.insertRow(i, viewer)
        if callback:
            self.viewerInserted.emit(self, i)

    def removeViewer(self, i: int, callback: bool = True):
        self.removeRow(i)
        if callback:
            self.viewerRemoved.emit(self, i)

    def renameViewer(self, i: int,  name: str, callback: bool = True):
        self.viewerItem(i).setName(name)
        if callback:
            self.viewerRenamed.emit(self, i, name)

    def appendLattice(self, i: int, callback: bool = True):
        lattice = QtViewerItem().setVTKLatticeItem()
        self.viewerItem(i).appendRow(lattice)
        if callback:
            self.viewerInserted.emit(self, self.viewerCount())

    def insertLattice(self, vtklattice: vtkLattice, i: int, j: int, callback: bool = True):
        lattice = QtViewerItem().setVTKLatticeItem(vtklattice)
        self.viewerItem(i).insertRow(j, lattice)
        if callback:
            self.latticeInserted.emit(self, i, j)

    def removeLattice(self, i: int, j: int, callback: bool = True):
        self.viewerItem(i).removeRow(j)
        if callback:
            self.latticeRemoved.emit(self, i, j)

    def nameChanged(self, item):
        if item.isVTKViewerItem():
            self.renameViewer(item.index().row(), item.name())