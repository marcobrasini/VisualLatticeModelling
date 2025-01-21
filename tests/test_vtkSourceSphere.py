from src.vtkLattice.lib.vtkSourceSphere import vtkSourceSphere
from . import render


class Test_vtkSourceSphere:

    center = (1.0, 0.0, 0.0)
    radius = 0.8
    resolution = (12, 24)

    def test__init__(self):
        sphere = vtkSourceSphere()

    def test_set_radius(self):
        sphere = vtkSourceSphere().set_radius(self.radius)
        assert sphere.source.GetRadius() == self.radius

    def test_radius(self):
        sphere = vtkSourceSphere().set_radius(self.radius)
        assert sphere.radius() == self.radius

    def test_set_center(self):
        sphere = vtkSourceSphere().set_center(self.center)
        assert sphere.source.GetCenter() == self.center

    def test_center(self):
        sphere = vtkSourceSphere().set_center(self.center)
        assert sphere.center() == self.center

    def test_set_resolution(self):
        sphere = vtkSourceSphere().set_resolution(*self.resolution)
        assert sphere.source.GetPhiResolution() == self.resolution[0]
        assert sphere.source.GetThetaResolution() == self.resolution[1]

    def test_resolution(self):
        sphere = vtkSourceSphere().set_resolution(*self.resolution)
        assert sphere.resolution() == self.resolution

    def test_set_resolution_int(self):
        sphere = vtkSourceSphere().set_resolution(self.resolution[0])
        assert sphere.source.GetPhiResolution() == self.resolution[0]
        assert sphere.source.GetThetaResolution() == 2*self.resolution[0]

    def test_resolution_int(self):
        sphere = vtkSourceSphere().set_resolution(self.resolution[0])
        assert sphere.resolution() == (self.resolution[0], 2*self.resolution[0])


@render
def test_rendering():

    from vtkmodules.vtkRenderingCore import vtkPolyDataMapper
    from src.vtkLattice.lib.vtkEntity import vtkEntity

    class vtkEntitySphere(vtkEntity):
        def __init__(self, source):
            self.source = source
            self.mapper = vtkPolyDataMapper()
            self.mapper.SetInputConnection(self.source.GetOutputPort())
            self.SetMapper(self.mapper)

    center = Test_vtkSourceSphere.center
    radius = Test_vtkSourceSphere.radius
    resolution = Test_vtkSourceSphere.resolution

    sphere = vtkSourceSphere()
    sphere.set_center(center)
    sphere.set_radius(radius)
    sphere.set_resolution(resolution[0])
    return vtkEntitySphere(sphere)
