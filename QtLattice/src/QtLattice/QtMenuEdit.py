from PyQt5.QtWidgets import QMenu, QAction
from .QtViewerModel import QtViewerModel
from .QtMenuEditLattice import QtMenuEditLattice
from .QtMenuEditCell import QtMenuEditCell


class QtMenuEdit(QMenu):

    def __init__(self, parent=None):
        super().__init__('Edit', parent=parent)
        self.addSeparator()
        self.lattice = QtMenuEditLattice(self)
        self.addAction(self.lattice.header)
        self.addAction(self.lattice.basis)
        self.addAction(self.lattice.atoms)
        self.addAction(self.lattice.bonds)
        self.addAction(self.lattice.polys)

        self.addSeparator()
        self.cell = QtMenuEditCell(self)
        self.addAction(self.cell.header)
        self.addAction(self.cell.transform)
        self.addAction(self.cell.supercell)
        self.addAction(self.cell.slabcell)

        self.addSeparator()
        self.reboot = QAction('Reboot...')
        self.addAction(self.reboot)
        self.rebase = QAction('Rebase...')
        self.addAction(self.rebase)

        self.aboutToShow.connect(self.selectValid)

    def model(self) -> QtViewerModel:
        return self.parent().model

    def selectValid(self):
        index = self.model().currentIndex()
        if len(index) > 1:
            lattice = self.model().currentLattice()
            self.cell.validCell(lattice)
            self.lattice.validLattice(lattice)
            self.reboot.setDisabled(False)
            self.rebase.setDisabled(False)
        else:
            self.cell.validCell(None)
            self.lattice.validLattice(None)
            self.reboot.setDisabled(True)
            self.rebase.setDisabled(True)
