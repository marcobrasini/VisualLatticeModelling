from unittest import TestCase
from src.QtLattice.QtLatticeSlab import QtLatticeSlab
from . import openqt


class TestQtLatticeSlab(TestCase):

    @openqt
    def test_QtLatticeSlab(self):
        return QtLatticeSlab()
