from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem
from vtkLattice import vtkLattice, vtkViewer


class QtViewerItem(QStandardItem):

    def __init__(self):
        super().__init__()
        self.vtk = None
        self.visible = Qt.Unchecked

    def name(self) -> str:
        return self.data(Qt.DisplayRole)

    def setName(self, name: str):
        self.setData(name, Qt.EditRole)

    def data(self, role=Qt.DisplayRole):
        if role in (Qt.DisplayRole, Qt.EditRole) and self.vtk is not None:
            return self.vtk.name
        return super().data(role)

    def setData(self, value, role=Qt.EditRole):
        if role in (Qt.DisplayRole, Qt.EditRole) and self.vtk is not None:
            self.vtk.name = value
        super().setData(value, role)

    # ':' (annotazione) e non '=' (valore di default)
    def setVTKLatticeItem(self, lattice: vtkLattice | str):
        if isinstance(lattice, str):
            lattice = vtkLattice.load_poscar(lattice)
        self.vtk = lattice
        self.setName(lattice.name)
        self.setCheckable(True)
        self.setCheckState(Qt.Checked)
        self.visible = self.checkState()
        return self

    def setVTKViewerItem(self, viewer: vtkViewer | str):
        if isinstance(viewer, str):
            viewer = vtkViewer(viewer)
        self.vtk = viewer
        self.setName(viewer.name)
        self.setCheckable(False)
        self.visible = self.checkState()
        for lattice in viewer:
            self.appendRow(QtViewerItem().setVTKLatticeItem(lattice))
        return self

    def isVTKViewerItem(self) -> bool:
        return isinstance(self.vtk, vtkViewer)

    def isVTKLatticeItem(self) -> bool:
        return isinstance(self.vtk, vtkLattice)
