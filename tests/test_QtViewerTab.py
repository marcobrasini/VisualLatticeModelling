from unittest import TestCase
from src.QtLattice.QtViewerModel import QtViewerModel
from src.QtLattice.QtViewerTab import QtViewerTab
from .test_QtViewerModel import TestQtViewerModel
from . import openqt


class TestQtMenu(TestCase):

    model = QtViewerModel()
    model.setupModel(TestQtViewerModel.vtkviewers)

    @openqt
    def test_QtViewerTab(self):
        tab = QtViewerTab()
        tab.setModel(self.model)
        return tab
