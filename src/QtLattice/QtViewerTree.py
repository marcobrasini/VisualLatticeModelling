import logging
from PyQt5.QtWidgets import QTreeView, QAbstractItemView
from PyQt5.QtCore import Qt, QObject, QModelIndex
from PyQt5.QtGui import QMouseEvent
from .QtViewerModel import QtViewerModel


class QtViewerTree(QTreeView):

    logger = logging.getLogger('qt')

    def __init__(self, model: QtViewerModel, parent: QObject = None):
        super().__init__(parent=parent)
        self.setModel(model)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

    def setup(self):
        pass

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        index = self.indexAt(event.pos())
        if not index.isValid():
            self.model().selectRoot()
        super().mouseDoubleClickEvent(event)

    def currentChanged(self, current: QModelIndex, previous: QModelIndex):
        if current.isValid():
            if self.model().itemFromIndex(current).isVTKViewerItem():
                self.model().selectViewer(current.row())
            if self.model().itemFromIndex(current).isVTKLatticeItem():
                self.model().selectLattice(current.parent().row(), current.row())
        super().currentChanged(current, previous)

    def selectRoot(self):
        self.clearSelection()
        self.setCurrentIndex(QModelIndex())
        self.logger.debug(
            f"  tree root selected.")

    def selectViewer(self, i: int):
        index = self.model().viewerItem(i).index()
        self.setCurrentIndex(index)
        self.logger.debug(
            f"  tree.viewer[{i}] selected.")

    def selectLattice(self, i: int, j: int):
        index = self.model().latticeItem(i, j).index()
        self.setCurrentIndex(index)
        self.logger.debug(
            f"  tree.viewer[{i}].lattice[{j}] selected.")
