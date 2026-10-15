from src.vtkLattice.lib.vtkSourcePolygon import vtkSourcePolygon
from . import render


class Test_vtkSourcePolygon:

    points = [[0., 0., 0.], [1., 1., 0.], [1., 0., 1.]]
    indices = [[0, 1, 2]]


@render
def test_rendering():

    from vtkmodules.vtkRenderingCore import vtkDataSetMapper
    from src.vtkLattice.lib.vtkEntity import vtkEntity

    class vtkEntityPolygon(vtkEntity):
        def __init__(self, source):
            self.source = source
            self.mapper = vtkDataSetMapper()
            self.mapper.SetInputConnection(self.source.GetOutputPort())
            self.SetMapper(self.mapper)
            self.GetProperty().SetColor(1.,0.,0.)
            self.GetProperty().SetLineWidth(2)

    points = Test_vtkSourcePolygon.points
    indices = Test_vtkSourcePolygon.indices

    polyhedron = vtkSourcePolygon()
    polyhedron.set_points(points)
    polyhedron.set_indices(indices)
    return vtkEntityPolygon(polyhedron)
