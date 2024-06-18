from PyQt5.QtWidgets import QMenu, QAction, QWidgetAction, QLabel
from PyQt5.QtCore import pyqtSignal
from .lib.MyDialog import MyDialogSign, MyDialogFile


class DialogLatticeLoad(MyDialogFile):
    def __init__(self, parent=None):
        super().__init__(MyDialogFile.LoadMode, parent=parent)
        self.setDirectory("tests/example")
        self.setNameFilters([
            "Any file (*)",
            "POSCAR file (*.vasp)",
        ])

class DialogLatticeSave(MyDialogFile):
    def __init__(self, parent=None):
        super().__init__(MyDialogFile.SaveMode, parent=parent)
        self.setDirectory("tests/example")
        self.setNameFilters([
            "Any file (*)",
            "POSCAR file (*.vasp)",
        ])

class DialogLatticeclose(MyDialogSign):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setWindowTitle('close lattice')
        self.setText('Do you want to close the lattice?')


class QtMenuItemLattice(QMenu):

    openLattice = pyqtSignal(list)
    loadLattice = pyqtSignal(list)
    saveLattice = pyqtSignal(list)
    closeLattice = pyqtSignal()

    def __init__(self, parent):
        super().__init__("Lattice...", parent=parent)
        self.addSeparator()
        self.header = QAction('Lattice...')
        self.header.setEnabled(False)
        #
        self.open = QAction('Open')
        self.open.triggered.connect(self.emit_openLattice)
        self.addAction(self.open)
        #
        self.load = QAction('Load')
        self.load.triggered.connect(self.emit_loadLattice)
        self.addAction(self.load)
        #
        self.save = QAction('Save')
        self.save.triggered.connect(self.emit_saveLattice)
        self.addAction(self.save)
        #
        self.close = QAction('Close')
        self.close.triggered.connect(self.emit_closeLattice)
        self.addAction(self.close)

    def validLattice(self, viewer, lattice):
        self.open.setEnabled(True)
        self.load.setDisabled(viewer is None)
        self.save.setDisabled(lattice is None)
        self.close.setDisabled(lattice is None)
        self.header.setText(f"Lattice {
            '' if lattice is None else lattice.name[:10]
        }...")

    def emit_openLattice(self):
        loadDialog = DialogLatticeLoad()
        if loadDialog.exec():
            files = loadDialog.selectedFiles()
            self.openLattice.emit(files)

    def emit_loadLattice(self):
        loadDialog = DialogLatticeLoad()
        if loadDialog.exec():
            files = loadDialog.selectedFiles()
            self.loadLattice.emit(files)

    def emit_saveLattice(self):
        saveDialog = DialogLatticeSave()
        if saveDialog.exec():
            files = saveDialog.selectedFiles()
            self.saveLattice.emit(files)

    def emit_closeLattice(self):
        closeDialog = DialogLatticeclose()
        if closeDialog.exec():
            self.closeLattice.emit()
