from unittest import TestCase
from src.QtLattice.QtTerminal import QtTerminal
from . import openqt


class Test_QtTerminal(TestCase):

    @openqt
    def test_QtTerminal(self):
        return QtTerminal()
