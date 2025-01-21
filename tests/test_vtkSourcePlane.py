from src.vtkLattice.lib.vtkSourcePlane import vtkSourcePlane
from . import render


class Test_vtkSourcePlane:

    origin = [0., 0., 0.]
    vectors = [[1, 0, 0], [1, 1, 0]]
    normal = [1, 1, 1]


@render
def test_rendering():

    from vtkmodules.vtkRenderingCore import vtkDataSetMapper
    from src.vtkLattice.lib.vtkEntity import vtkEntity

    class vtkEntityPlane(vtkEntity):
        def __init__(self, source):
            self.source = source
            self.mapper = vtkDataSetMapper()
            self.mapper.SetInputConnection(self.source.GetOutputPort())
            self.SetMapper(self.mapper)
            self.GetProperty().SetColor(1.,0.,0.)

    origin = Test_vtkSourcePlane.origin
    vectors = Test_vtkSourcePlane.vectors
    normal = Test_vtkSourcePlane.normal

    plane = vtkSourcePlane()
    plane.set_origin(origin)
    plane.set_vectors(*vectors)
    plane.set_normal(normal)
    return vtkEntityPlane(plane)
