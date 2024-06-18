from unittest import TestCase
from src.QtLattice.QtViewer import QtViewer
from .test_QtViewerModel import TestQtViewerModel
from . import openqt, Example


class TestQtViewer(TestCase):

    vtkviewers = TestQtViewerModel.exampleViewers(TestQtViewerModel)

    @openqt
    def test_QtViewer(self):
        qtviewer = QtViewer()
        qtviewer.setup(self.vtkviewers)
        return qtviewer
