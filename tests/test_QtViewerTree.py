from unittest import TestCase
from src.QtLattice.QtViewerModel import QtViewerModel
from src.QtLattice.QtViewerTree import QtViewerTree
from .test_QtViewerModel import TestQtViewerModel
from . import openqt


class TestQtViewerModel(TestCase):

    model = QtViewerModel()
    model.setupModel(TestQtViewerModel.vtkviewers)

    @openqt
    def test_QtViewerModel(self):
        view = QtViewerTree()
        view.setModel(self.model)
        return view
