from PyQt5.QtWidgets import QTreeView, QMenu, QAction, QAbstractItemView
from PyQt5.QtCore import Qt, QPoint, QObject, pyqtSignal


class QtViewerTree(QTreeView):

    removeLattice = pyqtSignal(QObject, int, int)

    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.customContextMenuRequested.connect(self.contextMenu)

    def contextMenu(self, point: QPoint):
        index = self.indexAt(point)
        if index.isValid():
            if index.internalPointer().isVTKLatticeItem():
                menu = QMenu(self)
                remove = QAction("Remove", self)
                remove.triggered.connect(lambda: self.emit_removeLattice(index))
                menu.addAction(remove)
                menu.exec(self.viewport().mapToGlobal(point))

    def emit_removeLattice(self, index):
        self.model().removeLattice(index.parent().row(), index.row())


