import sys
from PyQt5.QtWidgets import QApplication


def qt(func):

    def using(*args, **kwargs):
        app = QApplication(sys.argv)
        func(*args, **kwargs)
        app.exit()

    return using


def openqt(func):

    def opening(*args, **kwargs):
        app = QApplication(sys.argv)
        widget = func(*args, **kwargs)
        widget.show()
        app.exit(app.exec())

    return opening


class Example:

    from Lattice import Lattice

    POSCAR = 'tests/example/POSCAR'
    poscar = 'tests/example/poscar.vasp'
    lattice = Lattice().load_poscar(poscar)
    lattice.bonds = lattice.bonds.make(lattice.atoms['Zr'], lattice.atoms['O'], 2.5)
    lattice.bonds = lattice.bonds.make(lattice.atoms['Si'], lattice.atoms['O'], 2.5)
    lattice.polys = lattice.polys.make(lattice.atoms['Zr'], lattice.atoms['O'], 6)
    lattice.polys = lattice.polys.make(lattice.atoms['Si'], lattice.atoms['O'], 4)
