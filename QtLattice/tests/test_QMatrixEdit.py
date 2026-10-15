from unittest import TestCase
from src.QtLattice.lib.MyMatrixEdit import MyMatrixEdit
from . import openqt


class Test_MyMatrixEdit(TestCase):

    @openqt
    def test_MyMatrixEdit(self):
        matrix = MyMatrixEdit([
            [0, 1, 2],
            [3, 4, 5],
        ])
        matrix.setDirection(0, 2)
        matrix.setSpacing(0, 0)
        return matrix
