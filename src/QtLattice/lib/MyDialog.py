from PyQt5.QtWidgets import QDialog, QFileDialog, QGridLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from ..lib.MyFormWidget import MyFormWidget


class MyDialog(QDialog):
    def __init__(self, widget, single=False, parent = None):
        super().__init__(parent=parent)
        self.widget = widget
        self.acceptButton = QPushButton('')
        self.rejectButton = QPushButton('')
        self.acceptButton.clicked.connect(self.accept)
        self.rejectButton.clicked.connect(self.reject)
        self.setLayout(QGridLayout())
        if single:
            self.layout().addWidget(self.widget, 0, 0, Qt.AlignCenter)
            self.layout().addWidget(self.acceptButton, 1, 0, Qt.AlignCenter)
        else:
            self.setLayout(QGridLayout())
            self.layout().addWidget(self.widget, 0, 0, 1, 2, Qt.AlignCenter)
            self.layout().addWidget(self.acceptButton, 1, 0, Qt.AlignCenter)
            self.layout().addWidget(self.rejectButton, 1, 1, Qt.AlignCenter)
        self.setContentsMargins(20, 20, 20, 20)

    def setDefaultButton(self, button: QDialog.DialogCode):
        if button == QDialog.Accepted:
            self.acceptButton.setAutoDefault(True)
        if button == QDialog.Rejected:
            self.rejectButton.setAutoDefault(True)
        return self

    def setAcceptButton(self, text):
        self.acceptButton.setText(text)
        return self

    def setRejectButton(self, text):
        self.rejectButton.setText(text)
        return self


class MyDialogInfo(MyDialog):
    def __init__(self, parent = None):
        super().__init__(QLabel(""), single=True, parent=parent)
        self.setDefaultButton(QDialog.Accepted)
        self.setAcceptButton("Ok")

    def text(self):
        return self.widget.text()

    def setText(self, text):
        self.widget.setText(text)


class MyDialogSign(MyDialog):
    def __init__(self, parent = None):
        super().__init__(QLabel(""), parent=parent)
        self.setDefaultButton(QDialog.Accepted)
        self.setAcceptButton("Yes")
        self.setRejectButton("No")

    def text(self):
        return self.widget.text()

    def setText(self, text):
        self.widget.setText(text)


class MyDialogForm(MyDialog):
    def __init__(self, parent = None):
        super().__init__(MyFormWidget(), parent=parent)
        self.setDefaultButton(QDialog.Accepted)
        self.setAcceptButton("Ok")
        self.setRejectButton("Cancel")

    def setupForm(self, form: dict):
        self.widget.clean()
        for item in form.items():
            self.widget.append(item)
    def labels(self):
        return [self.widget.label(i) for i in self.widget.count()]

    def fields(self):
        return [self.widget.field(i) for i in range(self.widget.count())]


class MyDialogFile(QFileDialog):

    LoadMode = QFileDialog.ExistingFiles
    SaveMode = QFileDialog.AnyFile

    def __init__(self, fileMode, parent=None):
        super().__init__(parent=parent)
        self.setViewMode(QFileDialog.Detail)
        self.setFileMode(fileMode)
