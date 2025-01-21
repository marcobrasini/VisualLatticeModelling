from src.vtkLattice.lib.vtkSourceCylinder import vtkSourceCylinder
from . import render


class Test_vtkSourceCylinder:

    radius = 0.2
    length = 1.5
    resolution = 12

    def test__init__(self):
        cylinder = vtkSourceCylinder()

    def tests_set_radius(self):
        cylinder = vtkSourceCylinder().set_radius(self.radius)
        assert cylinder.source.GetRadius() == self.radius

    def test_radius(self):
        cylinder = vtkSourceCylinder().set_radius(self.radius)
        assert cylinder.radius() == self.radius

    def tests_set_length(self):
        cylinder = vtkSourceCylinder().set_length(self.length)
        assert cylinder.source.GetHeight() == self.length

    def test_length(self):
        cylinder = vtkSourceCylinder().set_length(self.length)
        assert cylinder.length() == self.length

    def tests_set_resolution(self):
        cylinder = vtkSourceCylinder().set_resolution(self.resolution)
        assert cylinder.source.GetResolution() == self.resolution

    def test_resolution(self):
        cylinder = vtkSourceCylinder().set_resolution(self.resolution)
        assert cylinder.resolution() == self.resolution


@render
def test_rendering():

    from vtkmodules.vtkRenderingCore import vtkPolyDataMapper
    from src.vtkLattice.lib.vtkEntity import vtkEntity

    class vtkEntityCylinder(vtkEntity):
        def __init__(self, source):
            self.source = source
            self.mapper = vtkPolyDataMapper()
            self.mapper.SetInputConnection(self.source.GetOutputPort())
            self.SetMapper(self.mapper)

    radius = Test_vtkSourceCylinder.radius
    length = Test_vtkSourceCylinder.length
    resolution = Test_vtkSourceCylinder.resolution

    cylinder = vtkSourceCylinder()
    cylinder.set_radius(radius)
    cylinder.set_length(length)
    cylinder.set_resolution(resolution)
    cylinder.orientate([1,1,0], axis=1)

    return vtkEntityCylinder(cylinder)
