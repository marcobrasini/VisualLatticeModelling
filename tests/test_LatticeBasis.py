import numpy as np

from src.Lattice.LatticeBasis import LatticeBasis
from . import Example


class Test_LatticeBasis:

    parameter = Example.parameter
    reduced = Example.reduced
    basis = Example.basis
    volume = np.linalg.det(basis)
    matrix = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [1/3, 1/3, 1/3],
    ])

    def test__init__(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert basis.parameter == self.parameter
        assert np.array_equal(basis, self.basis)

    def test__init__default(self):
        basis = LatticeBasis()
        assert basis.parameter == 1.0
        assert np.array_equal(basis, np.identity(3))

    def test__init__default_parameter(self):
        basis = LatticeBasis(self.basis)
        assert basis.parameter == 1.0
        assert np.array_equal(basis, self.basis)

    def test_reduced(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert np.array_equal(basis.reduced(), self.reduced)

    def test_a(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert basis.a() == np.linalg.norm(self.basis[0])

    def test_b(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert basis.b() == np.linalg.norm(self.basis[1])

    def test_c(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert basis.c() == np.linalg.norm(self.basis[2])

    def test_alpha(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert np.isclose(basis.alpha(), 90)

    def test_beta(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert np.isclose(basis.beta(), 90)

    def test_gamma(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert np.isclose(basis.gamma(), 60)

    def test_volume(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        assert np.isclose(basis.volume(), np.linalg.det(self.basis))

    def test_transform(self):
        basis = LatticeBasis(self.reduced, parameter=self.parameter)
        basis = basis.transform(self.matrix)
        assert isinstance(basis, LatticeBasis)
        assert np.array_equal(basis, self.matrix @ self.basis)
        assert basis.parameter == self.parameter
