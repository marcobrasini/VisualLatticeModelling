from unittest import TestCase
from src.QtLattice.QtViewer import QtViewer
from .test_QtViewerModel import TestQtViewerModel
from . import openqt


class TestQtViewer(TestCase):

    vtkviewers = TestQtViewerModel.vtkviewers

    @openqt
    def test_QtViewer(self):
        qtviewer = QtViewer()
        qtviewer.setupModel(self.vtkviewers)
        qtviewer.model.insertViewer(self.vtkviewers[1], 3)
        qtviewer.model.removeViewer(3)
        return qtviewer
