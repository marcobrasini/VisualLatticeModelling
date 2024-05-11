from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkCommonDataModel import vtkPolyData, vtkPolygon, vtkCellArray
from ..lib.vtkSource import vtkSource


class vtkSourcePolygon(vtkSource):

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
        polygons = vtkCellArray()
        for index in indices:
            polygon = vtkPolygon()
            polygon.GetPointIds().SetNumberOfIds(len(index))
            [polygon.GetPointIds().SetId(i, i) for i in range(len(index))]
            polygons.InsertNextCell(polygon)
        self.source.SetPolys(polygons)
