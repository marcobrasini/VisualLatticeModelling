from unittest import TestCase
from src.QtLattice.QtViewerTab import QtViewerTab
from .test_QtViewerModel import TestQtViewerModel
from . import openqt


class TestQtMenu(TestCase):

    model = TestQtViewerModel.exampleModel(TestQtViewerModel)

    @openqt
    def test_QtViewerTab(self):
        tab = QtViewerTab()
        tab.setModel(self.model)
        return tab
