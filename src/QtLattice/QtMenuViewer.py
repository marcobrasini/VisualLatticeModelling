from PyQt5.QtWidgets import QMenu, QAction, QWidgetAction, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
from .lib.MyDialog import MyDialogSign, MyDialogForm, MyDialogFile


class DialogViewerOpen(MyDialogForm):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setWindowTitle('Open viewer')
        self.setupForm({
            "Viewer name": QLineEdit()
        })

class DialogViewerClose(MyDialogSign):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setWindowTitle('Close viewer')
        self.setText('Do you want to close the viewer?')

class DialogViewerPrint(MyDialogFile):
    def __init__(self, parent = None):
        super().__init__(MyDialogFile.SaveMode, parent=parent)
        self.setDirectory("tests/example")
        self.setNameFilters([
            "Any file (*)",
        ])


class QtMenuViewer(QMenu):

    openViewer = pyqtSignal(str)
    renameViewer = pyqtSignal()
    printViewer = pyqtSignal(list)
    closeViewer = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__("Viewer...", parent=parent)
        #
        self.open = QAction("Open")
        self.open.triggered.connect(self.emit_openViewer)
        self.addAction(self.open)
        #
        self.rename = QAction("Rename")
        self.rename.triggered.connect(self.emit_renameViewer)
        self.addAction(self.rename)
        #
        self.print = QAction("Print")
        self.print.triggered.connect(self.emit_printViewer)
        self.addAction(self.print)
        #
        self.close = QAction("Close")
        self.close.triggered.connect(self.emit_closeViewer)
        self.addAction(self.close)


    def emit_openViewer(self):
        openDialog = DialogViewerOpen(self)
        if openDialog.exec():
            name = openDialog.fields()[0].text()
            self.openViewer.emit(name)
            print('openViewer emitted', name)

    def emit_renameViewer(self):
        self.renameViewer.emit()

    def emit_printViewer(self):
        printDialog = DialogViewerPrint(self)
        if printDialog.exec():
            files = printDialog.selectedFiles()
            self.printViewer.emit(files)
            print('printViewer emitted', files)

    def emit_closeViewer(self):
        closeDialog = DialogViewerClose(self)
        if closeDialog.open():
            self.closeViewer.emit()
            print('closeViewer emitted')
