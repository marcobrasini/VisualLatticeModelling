from PyQt5.QtWidgets import QWidget, QVBoxLayout
from .QtLatticeSlabPlane import QtLatticeSlabPlane
from .QtLatticeSlabTermination import QtLatticeSlabTermination


class QtLatticeSlab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.plane = QtLatticeSlabPlane()
        self.termination = QtLatticeSlabTermination()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.plane)
        self.layout().addWidget(self.termination)