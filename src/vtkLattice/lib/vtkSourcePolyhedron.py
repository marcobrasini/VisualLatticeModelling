from vtkmodules.vtkCommonCore import vtkPoints, vtkIdList
from vtkmodules.vtkCommonDataModel import vtkConvexPointSet
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid, VTK_POLYHEDRON
from ..lib.vtkSource import vtkSource


class vtkSourcePolyhedron(vtkSource):

    def __init__(self, convex=True):
        super().__init__()
        self.convex = convex
        self.source = vtkUnstructuredGrid()
        self.SetInputData(self.source)

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

    def set_convex(self):
        convex = vtkConvexPointSet()
        for i in range(len(self.points)):
            convex.GetPointIds().InsertId(i, i)
        self.source.Reset()
        self.source.InsertNextCell(convex.GetCellType(), convex.GetPointIds())
