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

class DialogLatticeRemove(MyDialogSign):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setWindowTitle('Remove lattice')
        self.setText('Do you want to remove the lattice?')


class QtMenuItemLattice(QMenu):

    openLattice = pyqtSignal(list)
    loadLattice = pyqtSignal(list)
    saveLattice = pyqtSignal(list)
    renameLattice = pyqtSignal()
    removeLattice = pyqtSignal()

    def __init__(self, parent):
        super().__init__("Lattice...", parent=parent)
        self.header = QWidgetAction(self)
        self.header.setDefaultWidget(QLabel('Lattice...'))
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
        self.rename = QAction('Rename')
        self.rename.triggered.connect(self.emit_renameLattice)
        self.addAction(self.rename)
        #
        self.remove = QAction('Remove')
        self.remove.triggered.connect(self.emit_removeLattice)
        self.addAction(self.remove)

    def validLattice(self, viewer, lattice):
        self.open.setEnabled(True)
        self.load.setEnabled(not viewer is None)
        self.save.setEnabled(not lattice is None)
        self.rename.setEnabled(not lattice is None)
        self.remove.setEnabled(not lattice is None)

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

    def emit_renameLattice(self):
        self.renameLattice.emit()

    def emit_removeLattice(self):
        closeDialog = DialogLatticeRemove()
        if closeDialog.exec():
            self.removeLattice.emit()
