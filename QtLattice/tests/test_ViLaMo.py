from unittest import TestCase
from src.QtLattice.ViLaMo import QtMain
from . import openqt


class TestQtMain(TestCase):

    @openqt
    def test_QtMain(self):
        return QtMain()
