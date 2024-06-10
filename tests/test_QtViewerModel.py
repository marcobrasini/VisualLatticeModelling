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
        model.insertViewer(2, vtkViewer('newViewer'))
        model.insertLattice(2, vtkLattice(Lattice('lattice_new')))
        model.removeLattice(0, 2)
        view = QTreeView()
        view.setModel(model)
        return view
