from vtkLattice import vtkLattice, vtkViewer
from PyQt5.QtCore import Qt, QAbstractItemModel, QModelIndex
from .QtViewerItem import QtViewerItem


class QtViewerModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self._root = QtViewerItem(None)
        self._root._data = ['root']

    # abstract methods
    def rowCount(self, parent: QModelIndex = QModelIndex()):
        item = parent.internalPointer() if parent.isValid() else self._root
        return item.childCount()

    def columnCount(self, parent: QModelIndex = QModelIndex()):
        item = parent.internalPointer() if parent.isValid() else self._root
        return item.dataCount()

    def index(self, row: int, column: int, parent: QModelIndex = QModelIndex()):
        if self.hasIndex(row, column, parent):
            item = parent.internalPointer() if parent.isValid() else self._root
            child = item.child(row)
            if child:
                return self.createIndex(row, column, child)
        return QModelIndex()

    def parent(self, index: QModelIndex):
        if index.isValid():
            item = index.internalPointer()
            parent = item.parent()
            if parent and parent != self._root:
                return self.createIndex(parent.row(), 0, parent)
        return QModelIndex()

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            item = index.internalPointer()
            return item.data(index.column())
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid():
            if role == Qt.EditRole:
                item = index.internalPointer()
                item.setData(value)
                self.dataChanged.emit(index, index, [Qt.DisplayRole])
                return True
        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.NoItemFlags
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return "QtViewer"
        return None

    # Custom methods
    def setupModel(self, viewerList):
        for viewer in viewerList:
            viewerItem = QtViewerItem(self._root)
            viewerItem.setVTKViewerItem(viewer)
            self._root.append(viewerItem)

    def addItem(self,
                parent: QtViewerItem|QModelIndex,
                index:  QModelIndex,
                item: QtViewerItem,
        ):
        if isinstance(parent, QModelIndex):
            parent = parent.internalPointer()
        self.beginInsertRows(index, index.row(), index.row())
        parent.insertChild(index.row(), item)
        self.endInsertRows()

    def delItem(self,
                parent: QtViewerItem|QModelIndex,
                index: QModelIndex
        ):
        if isinstance(parent, QModelIndex):
            parent = parent.internalPointer()
        self.beginInsertRows(index, index.row(), index.row())
        parent.removeChild(index.row())
        self.endInsertRows()

    def viewer(self, index: int) -> QModelIndex:
        return self.index(index, 0)

    def lattice(self, viewer: QModelIndex, index: int) -> QModelIndex:
        return self.index(index, 0, viewer)

    def insertViewer(self, index: int, vtkviewer: vtkViewer):
        viewer = self.createIndex(index, 0, self._root)
        item = QtViewerItem(self._root).setVTKViewerItem(vtkviewer)
        self.addItem(self._root, viewer, item)

    def removeViewer(self, index: int):
        viewer = self.viewer(index)
        self.delItem(self._root, viewer)

    def insertLattice(self, index: int, vtklattice: vtkLattice):
        viewer = self.viewer(index).internalPointer()
        lattice = self.createIndex(viewer.childCount(), 0, viewer)
        item = QtViewerItem(viewer).setVTKLatticeItem(vtklattice)
        self.addItem(viewer, lattice, item)

    def removeLattice(self, viewer: int, index: int):
        viewer = self.viewer(viewer)
        lattice = self.lattice(viewer, index)
        self.delItem(viewer, lattice)
