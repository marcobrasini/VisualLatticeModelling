from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor
from .lib.vtkSourcePolyline import vtkSourcePolyline
from .lib.vtkEntity import vtkEntity


class vtkLatticeCell(vtkEntity):

    points = [[0, 0, 0],
              [1, 0, 0],
              [0, 1, 0],
              [0, 0, 1],
              [1, 1, 0],
              [1, 0, 1],
              [0, 1, 1],
              [1, 1, 1]]
    indices = [[0, 1, 4, 2, 0],
               [0, 2, 6, 3, 0],
               [0, 3, 5, 1, 0],
               [7, 4, 1, 5, 7],
               [7, 5, 3, 6, 7],
               [7, 6, 2, 4, 7]]

    def __init__(self, basis):
        self.source = vtkSourcePolyline()
        self.source.set_points(vtkLatticeCell.points @ basis)
        self.source.set_indices(vtkLatticeCell.indices)
        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)

    def color(self):
        return self.actor.GetProperty().GetColor()

    def width(self):
        return self.actor.GetProperty().GetLineWidth()

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self

    def set_width(self, width):
        self.actor.GetProperty().SetLineWidth(width)
        return self
