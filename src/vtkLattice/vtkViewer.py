# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import vtkRenderer
from .vtkLattice import vtkLattice
from .vtkViewerController import vtkViewerController


class vtkViewer(QVTKRenderWindowInteractor):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.lattice = []
        self.renderer = vtkRenderer()
        self.renderer.SetBackground((1.0, 1.0, 1.0))
        self.renderer.ResetCamera()
        self.renderer.GetActiveCamera().ParallelProjectionOn()
        self.renderer.GetActiveCamera().SetPosition(0, 0, 1000)
        self.GetRenderWindow().AddRenderer(self.renderer)
        self.controller = vtkViewerController()
        self.controller.SetDefaultRenderer(self.renderer)
        self.interactor = self.GetRenderWindow().GetInteractor()
        self.interactor.SetInteractorStyle(self.controller)
        self.interactor.Initialize()

    def load_lattice(self, vtklattice: vtkLattice):
        vtklattice.render(self.renderer)
        self.lattice.append(vtklattice)
        return self
