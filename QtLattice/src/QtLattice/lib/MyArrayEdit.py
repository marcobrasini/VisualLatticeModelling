from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QBoxLayout
from ..lib.MyFloatFormatter import MyFloatFormatter
from ..lib.MyFloatEdit import MyFloatEdit


class MyArrayEdit(QWidget):

    valueChanged = pyqtSignal(QObject, int)

    def __init__(self,
                 array: list = None,
                 parent: QObject = None,
                 formatter: MyFloatFormatter = None,
                 direction: QBoxLayout.Direction = QBoxLayout.LeftToRight,
                 ):
        QWidget.__init__(self, parent=parent)
        self.widget = []
        self.formatter = MyFloatFormatter() if formatter is None else formatter
        self.layout = QBoxLayout(direction)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        if not array is None:
            self.setArray(array)

    def __getitem__(self, item):
        return self.widget[item]

    def emit_valueChanged(self, widget):
        i = self.widget.index(widget)
        self.valueChanged.emit(self, i)

    def append(self, value: float = None):
        widget = MyFloatEdit(value, formatter=self.formatter)
        widget.valueChanged.connect(self.emit_valueChanged)
        self.widget.append(widget)
        self.layout.addWidget(widget)
        return self

    def insert(self, index: int, value: float = None):
        widget = MyFloatEdit(value, formatter=self.formatter)
        widget.valueChanged.connect(self.emit_valueChanged)
        self.widget.insert(index, widget)
        self.layout.insertWidget(index, widget)
        return self

    def remove(self, index: int):
        self.layout.removeWidget(self.widget[index])
        del self.widget[index]
        return self

    def reset(self):
        [self.remove(0) for i in range(len(self.widget))]
        return self

    def clean(self):
        [widget.clean() for widget in self.widget]
        return self

    def value(self) -> list:
        value = [widget.value() for widget in self.widget]
        return value

    def setValue(self, value: list):
        for i, widget in enumerate(self.widget):
            widget.setValue(value[i])
        return self

    def setArray(self, array):
        self.reset()
        for value in array:
            self.append(value)
        return self

    def direction(self):
        return self.layout.direction()

    def setDirection(self, direction: QBoxLayout.Direction):
        self.layout.setDirection(direction)
        return self

    def spacing(self) -> int:
        return self.layout.spacing()

    def setSpacing(self, spacing: int):
        self.layout.setSpacing(spacing)
        return self
