from unittest import TestCase
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from src.QtLattice.QtMenu import QtMenu
from . import openqt


class TestQtMenu(TestCase):
    class Widget(QWidget):
        def __init__(self, menu, parent=None):
            super().__init__(parent=parent)
            self.menu = menu
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.contextMenu)

        def contextMenu(self, position):
            self.menu(self).exec_(self.mapToGlobal(position))

    @openqt
    def test_QtMain(self):
        return TestQtMenu.Widget(QtMenu)

