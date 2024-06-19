from unittest import TestCase
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeView, QHeaderView, QStyledItemDelegate
from src.QtLattice.QtLatticeSlabTerminationModel import QtLatticeSlabTerminationModel
from src.QtLattice.lib.MyFloatEdit import MyFloatEdit
from . import openqt, Example


class QtLatticeSlabDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = MyFloatEdit(parent=parent)
        return editor

    def setEditorData(self, editor: MyFloatEdit, index):
        value = index.model().data(index, Qt.EditRole)
        editor.setValue(editor.formatter.string_to_float(value))

    def setModelData(self, editor, model, index):
        value = editor.formatter.float_to_string(editor.value())
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class TestQtLatticeSlabModel(TestCase):

    lattice = Example.lattice

    @openqt
    def test_QtLatticeSlabModel(self):

        layers = [
            [
                self.lattice.atoms[0],
                self.lattice.atoms[-1],
                self.lattice.polys[-1]
            ],
            [
                self.lattice.polys[2],
                self.lattice.polys[0],
        ]]
        model = QtLatticeSlabTerminationModel()
        for layer in layers:
            model.appendLayer(layer)

        delegate = QtLatticeSlabDelegate()

        view = QTreeView()
        view.setModel(model)

        view.setItemDelegateForColumn(3, delegate)
        view.setItemDelegateForColumn(4, delegate)
        view.setItemDelegateForColumn(5, delegate)
        view.header().setSectionResizeMode(3, QHeaderView.Fixed)
        view.header().setSectionResizeMode(4, QHeaderView.Fixed)
        view.header().setSectionResizeMode(5, QHeaderView.Fixed)
        return view
