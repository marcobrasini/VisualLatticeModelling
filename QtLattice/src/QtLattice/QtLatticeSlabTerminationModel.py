from PyQt5.QtGui import QStandardItemModel
from .QtLatticeSlabTerminationItem import QtLatticeSlabTerminationItem


class QtLatticeSlabTerminationModel(QStandardItemModel):

    def __init__(self):
        super().__init__()
        self.root = self.invisibleRootItem
        self.setHorizontalHeaderLabels([
            'Layer',
            'Atom',
            'Name',
            'x',
            'y',
            'z'
        ])

    def setup(self, model):
        self.clear()
        self.setHorizontalHeaderLabels([
            'Layer',
            'Atom',
            'Name',
            'x',
            'y',
            'z'
        ])
        for layer in model:
            self.appendLayer(layer)

    def appendLayer(self, layer):
        layerItem = QtLatticeSlabTerminationItem.layerItem(layer)
        self.appendRow(layerItem)

    def removeLayer(self, i: int):
        self.removeRow(i)
