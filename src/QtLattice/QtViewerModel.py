from PyQt5.QtCore import Qt, QAbstractItemModel, QModelIndex
from .QtViewerItem import QtViewerItem


class QtViewerModel(QAbstractItemModel):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.root = QtViewerItem(None)
        self.root._data = ['root']

    def setupModel(self, viewerList):
        for viewer in viewerList:
            viewerItem = QtViewerItem(self.root)
            viewerItem.VTKViewerItem(viewer)
            self.root.append(viewerItem)

    def rowCount(self, parent: QModelIndex = QModelIndex()):
        item = parent.internalPointer() if parent.isValid() else self.root
        return item.childCount()

    def columnCount(self, parent: QModelIndex = QModelIndex()):
        item = parent.internalPointer() if parent.isValid() else self.root
        return item.dataCount()

    def index(self, row: int, column: int, parent: QModelIndex = QModelIndex()):
        if self.hasIndex(row, column, parent):
            item = parent.internalPointer() if parent.isValid() else self.root
            child = item.child(row)
            if child:
                return self.createIndex(row, column, child)
        return QModelIndex()

    def parent(self, index: QModelIndex):
        if index.isValid():
            item = index.internalPointer()
            parent = item.parent()
            if parent and parent != self.root:
                return self.createIndex(parent.row(), 0, parent)
        return QModelIndex()

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            item = index.internalPointer()
            return item.data(index.column())
        return None
