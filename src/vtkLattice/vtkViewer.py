from PyQt5.QtWidgets import QWidget
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import vtkRenderer
from .vtkLattice import vtkLattice
from .vtkViewerController import vtkViewerController
from .vtkViewerCamera import vtkViewerCamera
from .vtkViewerPrinter import vtkViewerPrinter


class vtkViewer(QVTKRenderWindowInteractor):

    def __init__(self,
                 parent: QWidget = None
                 ):
        super().__init__(parent)
        self.name = ""
        self.lattice = []
        self.renderer = vtkRenderer()
        self.renderer.SetBackground((1.0, 1.0, 1.0))
        self.renderer.ResetCamera()
        self.renderer.GetActiveCamera().ParallelProjectionOn()
        self.renderer.GetActiveCamera().SetPosition(0, 0, 1000)
        self.GetRenderWindow().AddRenderer(self.renderer)

        self.camera = vtkViewerCamera(self.renderer)
        self.camera.SetInteractor(self.GetRenderWindow().GetInteractor())
        self.camera.EnabledOn()

        self.printer = vtkViewerPrinter()
        self.printer.windowFilter.SetInput(self.GetRenderWindow())

        self.controller = vtkViewerController(self)
        self.controller.SetDefaultRenderer(self.renderer)
        self.interactor = self.GetRenderWindow().GetInteractor()
        self.interactor.SetInteractorStyle(self.controller)
        self.interactor.Initialize()

    def load_lattice(self, vtklattice: vtkLattice):
        vtklattice.render(self.renderer)
        self.lattice.append(vtklattice)
        if not self.name:
            self.name = vtklattice.name
        return self

    def close(self):
        self.Finalize()
        super().close()
