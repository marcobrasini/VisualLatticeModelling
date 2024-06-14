from PyQt5.QtWidgets import QMenu, QAction, QLabel, QWidgetAction
from .QtMenuViewer import QtMenuViewer
from .QtMenuLattice import QtMenuLattice


class QtMenuFile(QMenu):

    def __init__(self, parent=None):
        super().__init__("File", parent=parent)
        #
        self.viewer = QtMenuViewer(self)
        self.addAction(self.viewer.open)
        self.addAction(self.viewer.rename)
        self.addAction(self.viewer.print)
        self.addAction(self.viewer.close)
        #
        self.lattice = QtMenuLattice(self)
