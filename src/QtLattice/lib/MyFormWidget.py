from PyQt5.QtWidgets import QWidget, QFormLayout


class MyFormWidget(QWidget):

    def __init__(self, items=[], parent = None):
        super().__init__(parent=parent)
        self.setLayout(QFormLayout())
        for label, widget in items:
            self.layout().addRow(label, widget)

    def count(self):
        return self.layout().rowCount()

    def append(self, item):
        self.layout().addRow(*item)

    def insert(self, item, i):
        self.layout().insertRow(i, *item)

    def remove(self, i):
        self.layout().removeRow(i)

    def clean(self):
        while self.count():
            self.remove(0)

    def label(self, i):
        return self.layout().itemAt(i, QFormLayout.LabelRole).widget()

    def field(self, i):
        return self.layout().itemAt(i, QFormLayout.FieldRole).widget()
