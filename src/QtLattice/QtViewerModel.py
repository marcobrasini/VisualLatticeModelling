from PyQt5.QtCore import QModelIndex, QObject, pyqtSignal
from PyQt5.QtGui import QStandardItemModel
from vtkLattice import vtkLattice, vtkViewer
from .QtViewerItem import QtViewerItem


class QtViewerModel(QStandardItemModel):

    viewerRemoved = pyqtSignal(QObject, int)
    viewerInserted = pyqtSignal(QObject, int)
    latticeRemoved = pyqtSignal(QObject, int, int)
    latticeInserted = pyqtSignal(QObject, int, int)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setHorizontalHeaderLabels(['QtViewer'])
        self.root = self.invisibleRootItem

    # Custom methods
    def setupModel(self, viewerList):
        for viewer in viewerList:
            viewerItem = QtViewerItem().setVTKViewerItem(viewer)
            self.root().appendRow(viewerItem)

    def printModel(self, *args):
        report = "QtViewer:\n"
        for i in range(self.root().rowCount()):
            viewer = self.itemViewer(i)
            report += f"\t[{i}]:\t{viewer.name()}\n"
            for j in range(viewer.rowCount()):
                lattice = self.itemLattice(i, j)
                report += f"\t\t[{j}]:\t{lattice.name()}\n"
        print(report)

    def itemViewer(self, i: int) -> QtViewerItem:
        return self.item(i)

    def itemLattice(self, i: int, j: int) -> QModelIndex:
        return self.item(i).child(j)

    def viewer(self, i: int) -> QModelIndex:
        return self.itemViewer(i).vtk

    def lattice(self, i: int, j: int) -> QModelIndex:
        return self.itemLattice(i, j).vtk

    def insertViewer(self, vtkviewer: vtkViewer, i: int, callback: bool = True):
        viewer = QtViewerItem().setVTKViewerItem(vtkviewer)
        self.insertRow(i, viewer)
        if callback:
            self.viewerInserted.emit(self, i)
    #
    def insertLattice(self, vtklattice: vtkLattice, i: int, j: int, callback: bool = True):
        lattice = QtViewerItem().setVTKLatticeItem(vtklattice)
        self.itemViewer(i).insertRow(j, lattice)
        if callback:
            self.latticeInserted.emit(self, i, j)

    def removeViewer(self, i: int, callback: bool = True):
        self.removeRow(i)
        if callback:
            self.viewerRemoved.emit(self, i)

    def removeLattice(self, i: int, j: int, callback: bool = True):
        self.itemViewer(i).removeRow(j)
        if callback:
            self.latticeRemoved.emit(self, i, j)
