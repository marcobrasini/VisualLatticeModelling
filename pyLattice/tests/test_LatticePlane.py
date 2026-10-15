import numpy as np
from src.pyLattice.LatticePlane import LatticePlane
from . import Example


class Test_LatticePlane:

    index = [4,-2,0]
    points = np.array([
        [-0.5, 0.0, 0.0],
        [+0.5, 0.0, 0.0],
    ])

    def test__init__(self):
        plane = LatticePlane(self.index)
        assert np.array_equal(plane.hkl, [2,-1,0])
        assert np.array_equal(plane.abc, [1,-2,0])

    def test__call__(self):
        plane = LatticePlane(self.index)
        assert np.array_equal(plane(self.points, d=-1), -1-self.points@plane.coeff())
        assert np.array_equal(plane(self.points, d=-1) > 0, [False, False])
        assert np.array_equal(plane(self.points, d=0), 0-self.points @ plane.coeff())
        assert np.array_equal(plane(self.points, d=0) > 0, [True, False])
        assert np.array_equal(plane(self.points, d=1), 1-self.points@plane.coeff())
        assert np.array_equal(plane(self.points, d=1) > 0, [True, True])

    def test_ncell(self):
        plane = LatticePlane(self.index)
        assert np.array_equal(plane.ncell(), [1, -2, 1])

    def test_coeff(self):
        plane = LatticePlane(self.index)
        assert np.array_equal(plane.coeff(), [1.0, -0.5, 0.0])
