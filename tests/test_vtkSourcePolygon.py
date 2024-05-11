from src.vtkLattice.lib.vtkSourcePolygon import vtkSourcePolygon
from . import render


class Test_vtkSourcePolygon:

    points = [[0., 0., 0.], [1., 1., 0.], [1., 0., 1.], [-1, -1., -1]]


@render
def test_rendering():

    from vtkmodules.vtkRenderingCore import vtkActor, vtkDataSetMapper
    from src.vtkLattice.lib.vtkEntity import vtkEntity

    class vtkEntityPolygon(vtkEntity):
        def __init__(self, source):
            self.source = source
            self.mapper = vtkDataSetMapper()
            self.mapper.SetInputConnection(self.source.GetOutputPort())
            self.actor = vtkActor()
            self.actor.SetMapper(self.mapper)
            self.actor.GetProperty().SetColor(1.,0.,0.)
            self.actor.GetProperty().SetLineWidth(2)

    points = Test_vtkSourcePolygon.points

    polyhedron = vtkSourcePolygon()
    polyhedron.set_points(points)
    return vtkEntityPolygon(polyhedron)
