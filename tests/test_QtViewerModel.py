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
        view = QTreeView()
        view.setModel(model)
        return view
