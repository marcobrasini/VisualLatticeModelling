from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import (
    vtkCellArray,
    vtkPolyData,
    vtkPolyLine
)
from ..lib.vtkSource import vtkSource


class vtkSourcePolyline(vtkSource):
    def __init__(self):
        super().__init__()
        self.source = vtkPolyData()
        self.SetInputData(self.source)

    def set_points(self, points):
        self.points = points
        vertices = vtkPoints()
        for point in self.points:
            vertices.InsertNextPoint(point)
        self.source.SetPoints(vertices)

    def set_indices(self, indices):
        self.indices = indices
        edges = vtkCellArray()
        for index in indices:
            edges.InsertNextCell(len(index))
            [edges.InsertCellPoint(i) for i in index]
        self.source.SetLines(edges)
