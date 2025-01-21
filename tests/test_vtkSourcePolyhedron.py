from src.vtkLattice.lib.vtkSourcePolyhedron import vtkSourcePolyhedron
from . import render


class Test_vtkSourcePolyhedron:

    points = [[0., 0., 0.], [1., 1., 0.], [1., 0., 1.], [0., 1., 1.]]
    indices = [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]]


@render
def test_rendering():

    from vtkmodules.vtkRenderingCore import vtkDataSetMapper
    from src.vtkLattice.lib.vtkEntity import vtkEntity

    class vtkEntityPolyhedron(vtkEntity):
        def __init__(self, source):
            self.source = source
            self.mapper = vtkDataSetMapper()
            self.mapper.SetInputConnection(self.source.GetOutputPort())
            self.SetMapper(self.mapper)
            self.GetProperty().SetColor(1.,0.,0.)
            self.GetProperty().SetLineWidth(2)

    points = Test_vtkSourcePolyhedron.points
    indices = Test_vtkSourcePolyhedron.indices

    polyhedron = vtkSourcePolyhedron()
    polyhedron.set_points(points)
    polyhedron.set_indices(indices)
    return vtkEntityPolyhedron(polyhedron)
