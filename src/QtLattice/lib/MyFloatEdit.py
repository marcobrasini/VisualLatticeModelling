from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from ..lib.MyFloatFormatter import MyFloatFormatter


class MyFloatEdit(QLineEdit):

    valueChanged = pyqtSignal(QObject)

    def __init__(self,
                 value: float = None,
                 parent: QObject = None,
                 formatter: MyFloatFormatter = None,
        ):
        QLineEdit.__init__(self, parent=parent)
        if formatter is None:
            formatter = MyFloatFormatter()
        self.formatter = formatter
        self.setValidator(self.formatter.validator)
        self.editingFinished.connect(self.evaluate)
        self.setWidth()
        self.setAlignment(Qt.AlignRight)
        if not value is None:
            self.setValue(value)

    def clean(self):
        self.setText('')

    def value(self):
        text = self.text()
        return self.formatter.string_to_float(text)

    def setValue(self, value):
        text = self.formatter.float_to_string(value)
        return self.setText(text)

    def evaluate(self):
        value = self.formatter.evaluate(self.text())
        self.setValue(value)
        self.valueChanged.emit(self)

    def setWidth(self, width: float = None):
        if width is None:
            width = 10 * (self.formatter.length-1)
        self.setFixedWidth(width)
        return self
