import numpy as np

from src.vtkLattice.lib.vtkSourceArrow import vtkSourceArrow
from src.vtkLattice.lib.vtkSource import vtkSource
from . import render


class Test_vtkSourceArrow:

    ratio = 0.3
    radius = (0.1, 0.15)
    resolution = (10, 12)
    origin = (-0.5, 0.0, 0.0)
    vector = (1.0, 1.0, 0.0)
    length = np.linalg.norm(vector)

    def test__init__(self):
        arrow = vtkSourceArrow()

    def test_length(self):
        arrow = vtkSourceArrow().set_vector(self.vector)
        assert np.allclose(arrow.length(), np.linalg.norm(self.vector))

    def test_set_vector(self):
        arrow = vtkSourceArrow().set_vector(self.vector)
        assert np.isclose(arrow.transformation.scale[0], self.length)
        for i in range(3):
            x = arrow.transformation.orientation.GetElement(0, i)
            assert np.isclose(x, self.vector[i]/self.length)

    def test_vector(self):
        arrow = vtkSourceArrow().set_vector(self.vector)
        assert np.allclose(arrow.vector(), self.vector)

    def test_origin(self):
        arrow = vtkSourceArrow().set_origin(self.origin)
        assert arrow.origin() == self.origin

    def test_set_origin(self):
        arrow = vtkSourceArrow().set_origin(self.origin)
        assert arrow.transformation.translation == self.origin

    def test_set_ratio(self):
        arrow = vtkSourceArrow().set_ratio(self.ratio)
        assert arrow.source.GetTipLength() == self.ratio

    def test_ratio(self):
        arrow = vtkSourceArrow().set_ratio(self.ratio)
        assert arrow.ratio() == self.ratio

    def test_set_radius(self):
        arrow = vtkSourceArrow().set_radius(*self.radius)
        assert arrow.source.GetShaftRadius() == self.radius[0]
        assert arrow.source.GetTipRadius() == self.radius[1]

    def test_radius(self):
        arrow = vtkSourceArrow().set_radius(*self.radius)
        assert arrow.radius() == self.radius

    def test_set_radius_float(self):
        arrow = vtkSourceArrow().set_radius(self.radius[0])
        assert arrow.source.GetShaftRadius() == self.radius[0]
        assert arrow.source.GetTipRadius() == 2*self.radius[0]

    def test_radius_float(self):
        arrow = vtkSourceArrow().set_radius(self.radius[0])
        assert arrow.radius() == (self.radius[0], 2*self.radius[0])

    def test_set_resolution(self):
        arrow = vtkSourceArrow().set_resolution(*self.resolution)
        assert arrow.source.GetShaftResolution() == self.resolution[0]
        assert arrow.source.GetTipResolution() == self.resolution[1]

    def test_resolution(self):
        arrow = vtkSourceArrow().set_resolution(*self.resolution)
        assert arrow.resolution() == self.resolution


@render
def test_rendering():

    from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper
    from src.vtkLattice.lib.vtkEntity import vtkEntity
    class vtkEntityArrow(vtkEntity):
        def __init__(self, source: vtkSource):
            self.source = source
            self.mapper = vtkPolyDataMapper()
            self.mapper.SetInputConnection(self.source.GetOutputPort())
            self.actor = vtkActor()
            self.actor.SetMapper(self.mapper)

    origin = Test_vtkSourceArrow.origin
    vector = Test_vtkSourceArrow.vector
    ratio = Test_vtkSourceArrow.ratio
    radius = Test_vtkSourceArrow.radius
    resolution = Test_vtkSourceArrow.resolution

    arrow = vtkSourceArrow()
    arrow.set_origin(origin)
    arrow.set_vector(vector)
    arrow.set_ratio(ratio)
    arrow.set_radius(radius[0])
    arrow.set_resolution(resolution[0])

    return vtkEntityArrow(arrow)
