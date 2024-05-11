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
        polygon = vtkPolygon()
        polygon.GetPointIds().SetNumberOfIds(len(self.points))
        for i in range(len(self.points)):
            polygon.GetPointIds().SetId(i, i)
        cell = vtkCellArray()
        cell.InsertNextCell(polygon)
        self.source.SetPolys(cell)
