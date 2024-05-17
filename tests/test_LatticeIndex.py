import numpy as np
from src.Lattice.LatticeIndex import LatticeIndex
from . import Example


class Test_LatticeIndex:

    index = np.array([6, 4, -3])
    zeros = np.array([6, 0, -3])

    def test__init__(self):
        index = LatticeIndex(self.index)
        assert index.dtype == int
        assert np.array_equal(index, self.index)

    def test__init__zeros(self):
        index = LatticeIndex(self.zeros)
        assert index.dtype == int
        assert np.array_equal(index, self.zeros)

    def test_ones(self):
        index = LatticeIndex(self.index)
        assert isinstance(index.ones(), LatticeIndex)
        assert index.ones().dtype == int
        assert np.array_equal(index.ones(), self.index)

    def test_ones_zeros(self):
        index = LatticeIndex(self.zeros)
        assert isinstance(index.ones(), LatticeIndex)
        assert index.ones().dtype == int
        assert np.array_equal(index.ones(), [6, 1, -3])

    def test_gcd(self):
        index = LatticeIndex(self.index)
        assert type(index.gcd()) == int
        assert index.gcd() == 1

    def test_gcd_zeros(self):
        index = LatticeIndex(self.zeros)
        assert type(index.gcd()) == int
        assert index.gcd() == 3

    def test_lcm(self):
        index = LatticeIndex(self.index)
        assert type(index.lcm()) == int
        assert index.lcm() == 12

    def test_lcm_zeros(self):
        index = LatticeIndex(self.zeros)
        assert type(index.lcm()) == int
        assert index.lcm() == 6

    def test_reduce(self):
        index = LatticeIndex(3 * self.index)
        assert isinstance(index.reduce(), LatticeIndex)
        assert index.reduce().dtype == int
        assert np.array_equal(index.reduce(), self.index)

    def test_reduce_zeros(self):
        index = LatticeIndex(self.zeros)
        assert isinstance(index.reduce(), LatticeIndex)
        assert index.reduce().dtype == int
        assert np.array_equal(index.reduce(), self.zeros / 3)

    def test_invert(self):
        index = LatticeIndex(self.index)
        assert isinstance(index.invert(), LatticeIndex)
        assert index.invert().dtype == int
        assert np.array_equal(index.invert(), [2, 3, -4])

    def test_invert_zeros(self):
        index = LatticeIndex(self.zeros)
        assert isinstance(index.invert(), LatticeIndex)
        assert index.invert().dtype == int
        assert np.array_equal(index.invert(), [1, 0, -2])
