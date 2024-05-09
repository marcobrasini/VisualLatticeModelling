from vtkmodules.vtkCommonCore import vtkPoints, vtkIdList
from vtkmodules.vtkCommonDataModel import VTK_POLYHEDRON
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid
from ..lib.vtkSource import vtkSource


class vtkSourcePolyhedron(vtkSource):

    def __init__(self,
                 points,
                 indices,
                 ):
        super().__init__()
        self.source = vtkUnstructuredGrid()
        self.SetInputData(self.source)
        self.set_points(points)
        self.set_indices(indices)

    def set_points(self, points):
        self.points = points
        vertices = vtkPoints()
        for point in self.points:
            vertices.InsertNextPoint(point)
        self.source.SetPoints(vertices)

    def set_indices(self, indices):
        self.indices = indices
        faces = vtkIdList()
        faces.InsertNextId(len(indices))
        for index in indices:
            faces.InsertNextId(len(index))
            [faces.InsertNextId(i) for i in index]
        self.source.InsertNextCell(VTK_POLYHEDRON, faces)
