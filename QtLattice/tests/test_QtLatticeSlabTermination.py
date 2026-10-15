from unittest import TestCase
from src.QtLattice.QtLatticeSlabTermination import QtLatticeSlabTermination
from . import openqt, Example


class TestQtLatticeSlabTermination(TestCase):

    lattice = Example.lattice

    @openqt
    def test_QtLatticeSlabTermination(self):

        layers = [
            [
                self.lattice.atoms[0],
                self.lattice.atoms[-1],
                self.lattice.polys[-1]
            ],[
                self.lattice.polys[2],
                self.lattice.polys[0],
            ]
        ]

        termination = QtLatticeSlabTermination()
        termination.setup(layers)
        return termination
