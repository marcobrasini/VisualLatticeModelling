from unittest import TestCase
from Lattice import Lattice
from vtkLattice import vtkLattice, vtkViewer
from src.QtLattice.QtViewerModel import QtViewerModel
from . import openqt


class TestQtViewerModel(TestCase):

    vtkviewerA = vtkViewer("vtkViewerA")
    vtkviewerA.load_lattice(vtkLattice(Lattice('lattice0')))
    vtkviewerA.load_lattice(vtkLattice(Lattice('lattice1')))
    vtkviewerA.load_lattice(vtkLattice(Lattice('lattice2')))

    vtkviewerB = vtkViewer("vtkViewerB")
    vtkviewerB.load_lattice(vtkLattice(Lattice('lattice3')))
    vtkviewerB.load_lattice(vtkLattice(Lattice('lattice4')))

    vtkviewerC = vtkViewer("vtkViewerC")
    # vtkviewerC.load_lattice(vtkLattice(Lattice('lattice5')))

    vtkviewers = [
        vtkviewerA,
        vtkviewerB,
        vtkviewerC,
    ]

    @openqt
    def test_QtViewerModel(self):

        from PyQt5.QtWidgets import QTreeView

        model = QtViewerModel()
        model.setupModel(self.vtkviewers)
        model.insertViewer(vtkViewer('newViewer'), 2)
        model.insertLattice(vtkLattice(Lattice('lattice_new')), 2, 0)
        model.removeViewer(3)
        view = QTreeView()
        view.setModel(model)
        return view
