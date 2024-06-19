from PyQt5.QtWidgets import QMenu, QAction
from .QtViewerModel import QtViewerModel


class QtMenuEditLattice(QMenu):

    def __init__(self, parent=None):
        super().__init__('Edit', parent=parent)
        self.addSeparator()
        self.header = QAction('Lattice...')
        self.header.setEnabled(False)

        self.basis = QAction('Basis')
        self.addAction(self.basis)

        self.atoms = QAction('Atoms')
        self.addAction(self.atoms)

        self.bonds = QAction('Bonds')
        self.addAction(self.bonds)

        self.polys = QAction('Polys')
        self.addAction(self.polys)

    def validLattice(self, lattice):
        self.basis.setDisabled(lattice is None)
        self.atoms.setDisabled(lattice is None)
        self.bonds.setDisabled(lattice is None)
        self.polys.setDisabled(lattice is None)
        self.header.setText(f"Lattice {
            '' if lattice is None else lattice.name[:10]
        }...")
