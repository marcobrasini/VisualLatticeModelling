from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QBoxLayout
from ..lib.MyFloatFormatter import MyFloatFormatter
from ..lib.MyArrayEdit import MyArrayEdit


class MyMatrixEdit(QWidget):

    valueChanged = pyqtSignal(QObject, int, int)
    orientation = {
        QBoxLayout.TopToBottom: QBoxLayout.LeftToRight,
        QBoxLayout.LeftToRight: QBoxLayout.TopToBottom,
    }

    def __init__(self,
                 matrix: list = None,
                 parent: QObject = None,
                 formatter: MyFloatFormatter = None,
                 direction: QBoxLayout.Direction = QBoxLayout.TopToBottom,
        ):
        super().__init__(parent=parent)
        self.layout = QBoxLayout(direction)
        self.widget = []
        self.formatter = MyFloatFormatter() if formatter is None else formatter
        self.layout = QBoxLayout(direction)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        if not matrix is None:
            self.setMatrix(matrix)

    def __getitem__(self, index):
        return self.widget[index]


    def emit_valueChanged(self, widget, i):
        j = self.widget.index(widget)
        self.valueChanged.emit(self, i, j)

    def append(self, array: list = None):
        widget = MyArrayEdit(
            array,
            formatter=self.formatter,
            direction=self.orientation[self.direction()[0]]
        )
        widget.valueChanged.connect(self.emit_valueChanged)
        self.widget.append(widget)
        self.layout.addWidget(widget)
        return self

    def insert(self, index: int, array: list = None):
        widget = MyArrayEdit(
            array,
            formatter=self.formatter,
            direction=self.orientation[self.direction()[0]]
        )
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

    def value(self):
        value = [widget.value() for widget in self.widget]
        return value

    def setValue(self, value: list):
        for i, widget in enumerate(self.widget):
            widget.setValue(value[i])
        return self

    def setMatrix(self, matrix: list):
        for array in matrix:
            self.append(array)

    def direction(self) -> tuple:
        direction = self.widget[0].direction() if len(self.widget) else None
        return self.layout.direction(), direction

    def setDirection(self, *direction: float):
        self.layout.setDirection(direction[0])
        if len(direction) > 1 and len(self.widget):
            [widget.setDirection(direction[1]) for widget in self.widget]
        return self

    def spacing(self) -> tuple:
        spacing = self.widget[0].spacing() if len(self.widget) else None
        return self.layout.spacing(), spacing

    def setSpacing(self, *spacing: float):
        self.layout.setSpacing(spacing[0])
        if len(spacing) > 1 and len(self.widget):
            [widget.setSpacing(spacing[1]) for widget in self.widget]
        return self
