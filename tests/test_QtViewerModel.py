from unittest import TestCase
from Lattice import Lattice
from vtkLattice import vtkLattice, vtkViewer
from src.QtLattice.QtViewerModel import QtViewerModel
from . import openqt, Example


class TestQtViewerModel(TestCase):

    def exampleViewers(cls):
        vtkviewerA = vtkViewer("vtkViewerA")
        vtkviewerA.appendLattice(vtkLattice.load_poscar(Example.poscar))
        vtkviewerA.appendLattice(vtkLattice.load_poscar(Example.POSCAR))
        vtkviewerB = vtkViewer("vtkViewerB")
        vtkviewerB.appendLattice(vtkLattice.load_poscar(Example.poscar))
        return [
            vtkviewerA,
            vtkviewerB,
        ]

    def exampleModel(cls):
        model = QtViewerModel()
        model.setupModel(cls.exampleViewers(cls))
        return model

    @openqt
    def test_QtViewerModel(self):

        from PyQt5.QtWidgets import QTreeView

        model = QtViewerModel()
        model.setupModel(self.exampleViewers())
        model.insertViewer(vtkViewer('vtkViewer_new'), 0)
        model.insertLattice(vtkLattice(Lattice('vtkLattice_new')), 0, 0)
        model.removeLattice(2, 1)
        model.printModel()

        view = QTreeView()
        view.setModel(model)
        return view
