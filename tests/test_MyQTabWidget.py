from unittest import TestCase
from src.QtLattice.lib.MyTabWidget import MyTabWidget
from . import openqt


class TestMyTabWidget(TestCase):

    @openqt
    def test_MyQtTabWidget(self):
        return MyTabWidget()
