from unittest import TestCase
from vtkLattice import vtkViewer, vtkLattice
from src.QtLattice.QtViewer import QtViewer
from .test_QtViewerModel import TestQtViewerModel
from . import openqt, Example


class TestQtViewer(TestCase):

    vtkviewers = TestQtViewerModel.exampleViewers(TestQtViewerModel)

    @openqt
    def test_QtViewer(self):
        qtviewer = QtViewer()
        qtviewer.setupModel([])
        qtviewer.model.insertViewer(vtkViewer('vtklatticeC'), 0)
        qtviewer.model.insertLattice(vtkLattice.load_poscar(Example.POSCAR), 0, 0)
        return qtviewer
