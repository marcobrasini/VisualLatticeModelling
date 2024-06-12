from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem
from vtkLattice import vtkLattice, vtkViewer


class QtViewerItem(QStandardItem):

    VTKRootItem = 0
    VTKViewerItem = 1
    VTKLatticeItem = 2

    def __init__(self, parent = None):
        super().__init__(parent)
        self.name = self.data
        self.setName = self.setData

    def data(self, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.vtk.name
        return super().data(role)

    def setData(self, value, role=Qt.EditRole):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            self.vtk.name = value
        return super().setData(value, role)

    def setVTKLatticeItem(self, lattice = None):
        if lattice is None:
            self.vtk = QtViewerItem.VTKLatticeItem
            return self
        self.vtk = lattice
        self.setData(lattice.name)
        self.setCheckable(True)
        self.setCheckState(Qt.Checked)
        return self

    def setVTKViewerItem(self, viewer = None):
        if viewer is None:
            self.vtk = QtViewerItem.VTKLatticeItem
            return self
        self.vtk = viewer
        self.setData(viewer.name)
        for lattice in viewer:
            latticeItem = QtViewerItem(self)
            latticeItem.setVTKLatticeItem(lattice)
            self.appendRow(latticeItem)
        return self

    def isVTKViewerItem(self):
        return (isinstance(self.vtk, vtkViewer)
                or self.vtk == self.VTKViewerItem)

    def isVTKLatticeItem(self):
        return (isinstance(self.vtk, vtkLattice)
                or self.vtk == self.VTKLatticeItem)
