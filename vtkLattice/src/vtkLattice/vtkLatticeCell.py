from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor
from .lib.vtkSourcePolyline import vtkSourcePolyline
from .lib.vtkEntity import vtkEntity


DEFAULT_COLOR = (0.0, 0.0, 0.0)
DEFAULT_WIDTH = 1.0


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
        self.SetMapper(self.mapper)
        self.set_color(DEFAULT_COLOR)
        self.set_linewidth(DEFAULT_WIDTH)
