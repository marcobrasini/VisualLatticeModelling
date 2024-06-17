from PyQt5.QtWidgets import QMenu
from .QtMenuItemViewer import QtMenuItemViewer
from .QtMenuItemLattice import QtMenuItemLattice


class QtMenuItem(QMenu):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        #
        self.viewer = QtMenuItemViewer(self)
        self.addAction(self.viewer.header)
        self.addAction(self.viewer.open)
        self.addAction(self.viewer.rename)
        self.addAction(self.viewer.print)
        self.addAction(self.viewer.close)
        #
        self.lattice = QtMenuItemLattice(self)
        self.addAction(self.lattice.header)
        self.addAction(self.lattice.open)
        self.addAction(self.lattice.load)
        self.addAction(self.lattice.save)
        self.addAction(self.lattice.rename)
        self.addAction(self.lattice.remove)

    def selectItem(self, viewer, lattice):
        self.viewer.validViewer(viewer)
        self.lattice.validLattice(viewer, lattice)
