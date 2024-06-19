from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QTreeView, QHeaderView, QStyledItemDelegate
from PyQt5.QtCore import Qt
from .lib.MyFloatEdit import MyFloatEdit
from .QtLatticeSlabTerminationModel import QtLatticeSlabTerminationModel



class QtLatticeSlabTermination(QGroupBox):

    class Delegate(QStyledItemDelegate):
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

    def __init__(self, parent=None):
        super().__init__("Termination", parent=parent)
        self.model = QtLatticeSlabTerminationModel()
        self.view = QTreeView()
        self.view.setModel(self.model)
        self.delegate = QtLatticeSlabTermination.Delegate()
        self.view.setItemDelegateForColumn(3, self.delegate)
        self.view.setItemDelegateForColumn(4, self.delegate)
        self.view.setItemDelegateForColumn(5, self.delegate)
        self.view.header().setSectionResizeMode(3, QHeaderView.Fixed)
        self.view.header().setSectionResizeMode(4, QHeaderView.Fixed)
        self.view.header().setSectionResizeMode(5, QHeaderView.Fixed)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.view)

    def setup(self, layers):
        self.model.setup(layers)