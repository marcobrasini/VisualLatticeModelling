from Lattice import LatticeAtom, LatticePoly
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import Qt
from .lib.MyFloatFormatter import MyFloatFormatter


class QtLatticeSlabTerminationItem(QStandardItem):

    formatter = MyFloatFormatter()

    def __init__(self, name):
        super().__init__(name)
        self.setCheckable(True)
        self.setCheckState(Qt.Checked)

    @classmethod
    def atomItem(cls, atom: LatticeAtom):
        item = [
            cls('Atom'),
            QStandardItem(atom.atom),
            QStandardItem(atom.name),
            QStandardItem(cls.formatter.float_to_string(atom.site[0])),
            QStandardItem(cls.formatter.float_to_string(atom.site[1])),
            QStandardItem(cls.formatter.float_to_string(atom.site[2])),
        ]
        return item

    @classmethod
    def polyItem(cls, poly: LatticePoly):
        item = cls('Poly')
        item.appendRow(cls.atomItem(poly.center))
        for atom in poly.atoms:
            item.appendRow(cls.atomItem(atom))
        return item

    @classmethod
    def layerItem(cls, layer):
        item = cls('Layer')
        for atoms in layer:
            if isinstance(atoms, LatticeAtom):
                item.appendRow(cls.atomItem(atoms))
            if isinstance(atoms, LatticePoly):
                item.appendRow(cls.polyItem(atoms))
        return item
