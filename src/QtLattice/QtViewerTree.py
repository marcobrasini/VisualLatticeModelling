from PyQt5.QtWidgets import QTreeView, QMenu, QAction, QAbstractItemView
from PyQt5.QtCore import Qt, QPoint, QObject, pyqtSignal
from vtkLattice import vtkLattice, vtkViewer
from .QtMenu import QtMenu

class QtViewerTree(QTreeView):

    viewerSelected = pyqtSignal(int)
    viewerRenamed = pyqtSignal(str)
    # removeLattice = pyqtSignal(QObject, int, int)

    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.customContextMenuRequested.connect(self.contextMenu)

    def selected(self):
        return self.selectedIndexes()[0]

    def contextMenu(self, point: QPoint):
        index = self.selected()
        if index:
            menu = QtMenu(self)
            menu.viewer.renameViewer.connect(
                lambda: self.renameViewer(index)
            )
            menu.exec(self.viewport().mapToGlobal(point))

    def renameViewer(self, index):
        if self.model().itemFromIndex(index).isVTKViewerItem():
            self.edit(index)
        else:
            self.edit(index.parent())

    def selectViewer(self, i: int):
        self.setCurrentIndex(self.model().createIndex(i, 0))

    def mouseDoubleClickEvent(self, e):
        index = self.currentIndex()
        if self.model().itemFromIndex(index).isVTKViewerItem():
            self.viewerSelected.emit(index.row())
        else:
            self.viewerSelected.emit(index.parent().row())
