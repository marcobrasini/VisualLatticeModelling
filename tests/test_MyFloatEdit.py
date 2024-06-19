from unittest import TestCase
from src.QtLattice.lib.MyFloatEdit import MyFloatEdit
from . import openqt, qt


class Test_MyFloatEdit(TestCase):

    @openqt
    def test_MyFloatEdit(self):
        return MyFloatEdit(1.8)
