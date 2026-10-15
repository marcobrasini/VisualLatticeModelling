from unittest import TestCase
from src.QtLattice.lib.MyArrayEdit import MyArrayEdit
from . import openqt


class Test_MyArrayEdit(TestCase):

    @openqt
    def test_QVectorEdit(self):
        array = MyArrayEdit([0, 1, 2])
        array.insert(1, 3)
        array.remove(0)
        array.setSpacing(8)
        return array
