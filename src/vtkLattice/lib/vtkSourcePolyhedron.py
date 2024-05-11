from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkConvexPointSet
from vtkmodules.vtkCommonDataModel import vtkUnstructuredGrid
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
        convex = vtkConvexPointSet()
        for i in range(len(self.points)):
            convex.GetPointIds().InsertId(i, i)
        self.source.SetPoints(vertices)
        self.source.InsertNextCell(convex.GetCellType(),
                                   convex.GetPointIds())
