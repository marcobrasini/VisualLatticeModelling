from PyQt5.QtCore import QModelIndex, QObject, pyqtSignal
from vtkLattice import vtkLattice, vtkViewer
from .QtViewerBase import QtViewerBase
from .QtViewerItem import QtViewerItem


class QtViewerModel(QtViewerBase):

    viewerRemoved = pyqtSignal(QObject, int)
    viewerInserted = pyqtSignal(QObject, int)
    latticeRemoved = pyqtSignal(QObject, int, int)
    latticeInserted = pyqtSignal(QObject, int, int)

    # Custom methods
    def setupModel(self, viewerList):
        for viewer in viewerList:
            viewerItem = QtViewerItem(self._root)
            viewerItem.setVTKViewerItem(viewer)
            self._root.append(viewerItem)

    def printModel(self, *args):
        print(f"QtViewer:")
        for i in range(self.root().childCount()):
            viewer = self.itemViewer(i)
            print(f"\t[{i}]:\t{viewer.name()}")
            for j in range(viewer.childCount()):
                lattice = self.itemLattice(i, j)
                print(f"\t\t[{j}]:\t{lattice.name()}")

    def indexViewer(self, i: int) -> QModelIndex:
        return self.index(i, 0)

    def indexLattice(self, i: int, j: int) -> QModelIndex:
        return self.index(j, 0, self.indexViewer(i))
    #
    def itemViewer(self, i: int) -> QModelIndex:
        return self.indexViewer(i).internalPointer()

    def itemLattice(self, i: int, j: int) -> QModelIndex:
        return self.indexLattice(i, j).internalPointer()

    def viewer(self, i: int) -> QModelIndex:
        return self.itemViewer(i).vtk()

    def lattice(self, i: int, j: int) -> QModelIndex:
        return self.itemLattice(i, j).vtk()

    def insertViewer(self, vtkviewer: vtkViewer, i: int, callback: bool = True):
        parent = self.root()
        viewer = self.createIndex(i, 0, parent)
        item = QtViewerItem(parent).setVTKViewerItem(vtkviewer)
        self.addItem(parent, viewer, item)
        if callback:
            self.viewerInserted.emit(self, i)

    def insertLattice(self, vtklattice: vtkLattice, i: int, j: int, callback: bool = True):
        parent = self.itemViewer(i)
        lattice = self.createIndex(j, 0, parent)
        item = QtViewerItem(parent).setVTKLatticeItem(vtklattice)
        self.addItem(parent, lattice, item)
        if callback:
            self.latticeInserted.emit(self, i, j)

    def removeViewer(self, i: int, callback: bool = True):
        parent = self.root()
        viewer = self.indexViewer(i)
        self.delItem(parent, viewer)
        if callback:
            self.viewerRemoved.emit(self, i)

    def removeLattice(self, i: int, j: int, callback: bool = True):
        parent = self.itemViewer(i)
        lattice = self.indexLattice(i, j)
        self.delItem(parent, lattice)
        if callback:
            self.latticeRemoved.emit(self, i, j)
