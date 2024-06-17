from PyQt5.QtCore import QModelIndex, QObject, pyqtSignal
from PyQt5.QtGui import QStandardItemModel
from vtkLattice import vtkLattice, vtkViewer
from .QtViewerItem import QtViewerItem


class QtViewerModel(QStandardItemModel):

    viewerSelected = pyqtSignal(QObject, int)
    viewerInserted = pyqtSignal(QObject, int)
    viewerExported = pyqtSignal(QObject, int)
    viewerRenamed = pyqtSignal(QObject, int, str)
    viewerRemoved = pyqtSignal(QObject, int)
    latticeSelected = pyqtSignal(QObject, int, int)
    latticeInserted = pyqtSignal(QObject, int, int)
    latticeExported = pyqtSignal(QObject, int, int)
    latticeRenamed = pyqtSignal(QObject, int, int, str)
    latticeRemoved = pyqtSignal(QObject, int, int)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.root = self.invisibleRootItem
        self.current = QModelIndex()
        self.setHorizontalHeaderLabels(['QtViewer'])
        self.itemChanged.connect(self.nameChanged)
        self.itemChanged.connect(self.visibilityChanged)

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

    def appendViewer(self, name: str, callback: bool = True):
        viewer = QtViewerItem().setVTKViewerItem(name)
        self.appendRow(viewer)
        if callback:
            self.viewerInserted.emit(self, self.viewerCount() - 1)

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

    def appendLattice(self, name: str, i: int, callback: bool = True):
        lattice = QtViewerItem().setVTKLatticeItem(name)
        self.viewerItem(i).appendRow(lattice)
        if callback:
            self.latticeInserted.emit(self, i, self.latticeCount(i) - 1)

    def insertLattice(self, vtklattice: vtkLattice, i: int, j: int, callback: bool = True):
        lattice = QtViewerItem().setVTKLatticeItem(vtklattice)
        self.viewerItem(i).insertRow(j, lattice)
        if callback:
            self.latticeInserted.emit(self, i, j)

    def removeLattice(self, i: int, j: int, callback: bool = True):
        self.viewerItem(i).removeRow(j)
        if callback:
            self.latticeRemoved.emit(self, i, j)

    def nameChanged(self, item: QtViewerItem):
        if item.isVTKViewerItem():
            self.renameViewer(item.index().row(), item.name())

    def visibilityChanged(self, item: QtViewerItem):
        if item.isVTKLatticeItem() and item.checkState() != item.visible:
            i, j = item.index().parent().row(), item.index().row()
            item.visible = item.checkState()
            self.lattice(i, j).visible(bool(item.visible))
