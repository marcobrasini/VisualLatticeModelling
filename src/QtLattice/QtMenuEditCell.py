from PyQt5.QtWidgets import QMenu, QAction
from .lib.MyDialog import MyDialogForm
from .lib.MyArrayEdit import MyArrayEdit
from .QtViewerModel import QtViewerModel


class DialogLatticeSupercell(MyDialogForm):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle('Lattice Supercell')
        self.setupForm({
            "Supercell index": MyArrayEdit(formatter="")
        })


class QtMenuEditCell(QMenu):

    def __init__(self, parent=None):
        super().__init__('Edit', parent=parent)
        self.addSeparator()
        self.header = QAction('Cell...')
        self.header.setEnabled(False)

        self.transform = QAction('Transform cell')
        self.addAction(self.transform)

        self.supercell = QAction('Super cell')
        self.addAction(self.supercell)

        self.slabcell = QAction('Slab cell')
        self.addAction(self.slabcell)

    def validCell(self, lattice):
        self.transform.setDisabled(lattice is None)
        self.supercell.setDisabled(lattice is None)
        self.slabcell.setDisabled(lattice is None)
