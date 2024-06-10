from unittest import TestCase
from vtkLattice import vtkLattice
from src.QtLattice.QtViewerModel import QtViewerModel
from src.QtLattice.QtViewerTab import QtViewerTab
from .test_QtViewerModel import TestQtViewerModel
from . import openqt, Example


class TestQtMenu(TestCase):

    lattice1 = vtkLattice(Example.lattice)
    lattice2 = vtkLattice.load_poscar(Example.POSCAR)
    model = QtViewerModel()
    model.setupModel(TestQtViewerModel.vtkviewers)

    @openqt
    def test_QtViewerTab(self):
        tab = QtViewerTab()
        tab.setModel(self.model)
        self.model.removeViewer(0)
        return tab

    # @openqt
    # def test_QtViewer_open(self):
    #     viewer = QtViewerTab()
    #     viewer.open_lattice(self.lattice1)
    #     return viewer
    #
    # @openqt
    # def test_QtViewer_load(self):
    #     viewer = QtViewerTab()
    #     viewer.load_lattice(self.lattice1)
    #     viewer.load_lattice(self.lattice2)
    #     return viewer
