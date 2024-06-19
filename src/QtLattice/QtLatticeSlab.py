from PyQt5.QtWidgets import QWidget, QVBoxLayout
from .QtLatticeSlabPlane import QtLatticeSlabPlane


class QtLatticeSlab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.plane = QtLatticeSlabPlane()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.plane)