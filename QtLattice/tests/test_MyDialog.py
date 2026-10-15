from unittest import TestCase
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QLineEdit
from src.QtLattice.lib.MyDialog import MyDialogInfo, MyDialogSign, MyDialogForm
from . import openqt


class TestMyDialog(TestCase):

    class Widget(QWidget):
        def __init__(self, dialog):
            super().__init__()
            self.dialog = dialog
            self.button = QPushButton('exec dialog')
            self.button.clicked.connect(self.dialog.exec)
            self.setLayout(QGridLayout())
            self.layout().addWidget(self.button)

    @openqt
    def test_MyDialogSign(self):
        dialog = MyDialogSign()

        dialog.setText("Do you confirm?")
        return TestMyDialog.Widget(dialog)

    @openqt
    def test_MyDialogInfo(self):
        dialog = MyDialogInfo()
        dialog.setText("This is a notification")
        return TestMyDialog.Widget(dialog)

    @openqt
    def test_MyDialogForm(self):
        dialog = MyDialogForm()
        dialog.setupForm({"First name": QLineEdit(),
                          "Last name":  QLineEdit()})
        return TestMyDialog.Widget(dialog)
