from src.vtkLattice.lib.vtkSourcePolyline import vtkSourcePolyline
from . import render


class Test_vtkSourcePolyline:

    points = [[0., 0., 0.], [1., 1., 0.], [1., 0., 1.], [0., 1., 1.]]
    indices = [[0,1,2,0], [1,2,3,1], [2,3,0,2], [3,0,1,3]]


@render
def test_rendering():

    from vtkmodules.vtkRenderingCore import vtkActor, vtkPolyDataMapper
    from src.vtkLattice.lib.vtkEntity import vtkEntity

    class vtkEntityPolyline(vtkEntity):
        def __init__(self, source):
            self.source = source
            self.mapper = vtkPolyDataMapper()
            self.mapper.SetInputConnection(self.source.GetOutputPort())
            self.actor = vtkActor()
            self.actor.SetMapper(self.mapper)
            self.actor.GetProperty().SetColor(1.,0.,0.)
            self.actor.GetProperty().SetLineWidth(2)

    points = Test_vtkSourcePolyline.points
    indices = Test_vtkSourcePolyline.indices

    polyline = vtkSourcePolyline()
    polyline.set_points(points)
    polyline.set_indices(indices)
    return vtkEntityPolyline(polyline)