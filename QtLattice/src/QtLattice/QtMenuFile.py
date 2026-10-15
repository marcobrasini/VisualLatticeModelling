from PyQt5.QtWidgets import QMenu, QAction, QWidgetAction
from PyQt5.QtCore import pyqtSignal
from .lib.MyDialog import MyDialogSign


class DialogExit(MyDialogSign):
    def __init__(self, parent = None):
        super().__init__(parent=parent)
        self.setWindowTitle('Exit')
        self.setText('Do you want to exit?')


class QtMenuFile(QMenu):

    exitSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__('File', parent=parent)
        for action in self.item().actions():
            self.addAction(action)
        self.aboutToShow.connect(self.item().selectValid)
        #
        self.addSeparator()
        self.exit = QAction('Exit')
        self.exit.triggered.connect(self.emit_exitSignal)
        self.addAction(self.exit)
        #

    def model(self):
        return self.parent().model

    def item(self):
        return self.parent().item

    def emit_exitSignal(self):
        exitDialog = DialogExit()
        if exitDialog.exec():
            self.exitSignal.emit()
