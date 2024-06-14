from PyQt5.QtWidgets import QMenu, QAction, QLabel, QWidgetAction
from .QtMenuViewer import QtMenuViewer
from .QtMenuLattice import QtMenuLattice


class QtMenu(QMenu):

    def __init__(self, parent=None):
        super().__init__("File", parent=parent)
        viewer = QWidgetAction(self)
        viewer.setDefaultWidget(QLabel('Viewer...'))
        viewer.setEnabled(False)
        self.addAction(viewer)
        self.viewer = QtMenuViewer(self)
        self.addAction(self.viewer.open)
        self.addAction(self.viewer.rename)
        self.addAction(self.viewer.print)
        self.addAction(self.viewer.close)
        #
        lattice = QWidgetAction(self)
        lattice.setDefaultWidget(QLabel('Lattice...'))
        lattice.setEnabled(False)
        self.addAction(lattice)
        self.lattice = QtMenuLattice(self)
        self.addAction(self.lattice.open)
        self.addAction(self.lattice.load)
        self.addAction(self.lattice.save)
        self.addAction(self.lattice.rename)
        self.addAction(self.lattice.remove)

