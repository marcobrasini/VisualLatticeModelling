from PyQt5.QtCore import Qt, QAbstractItemModel, QModelIndex
from .QtViewerItem import QtViewerItem


class QtViewerBase(QAbstractItemModel):

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

    def root(self):
        return self._root

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

    def addItem(self,
                parent: QtViewerItem,
                index:  QModelIndex,
                item: QtViewerItem,
        ):
        self.beginInsertRows(index.parent(), index.row(), index.row())
        parent.insertChild(index.row(), item)
        self.endInsertRows()

    def delItem(self,
                parent: QtViewerItem,
                index: QModelIndex
        ):
        self.beginRemoveRows(index.parent(), index.row(), index.row())
        parent.removeChild(index.row())
        self.endRemoveRows()
