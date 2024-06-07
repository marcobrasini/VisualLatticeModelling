from PyQt5.QtWidgets import QWidget
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import vtkRenderer
from .vtkLattice import vtkLattice
from .vtkWidgetController import vtkWidgetController
from .vtkWidgetCamera import vtkWidgetCamera
from .vtkWidgetPrinter import vtkWidgetPrinter
from .vtkViewer import vtkViewer


class vtkWidget(QVTKRenderWindowInteractor):

    def __init__(self,
                 viewer: vtkViewer,
                 parent: QWidget = None
                 ):
        super().__init__(parent=parent)
        self.viewer = viewer
        self.renderer = vtkRenderer()
        self.renderer.SetBackground((1.0, 1.0, 1.0))
        self.renderer.ResetCamera()
        self.renderer.GetActiveCamera().ParallelProjectionOn()
        self.renderer.GetActiveCamera().SetPosition(0, 0, 1000)
        self.GetRenderWindow().AddRenderer(self.renderer)

        self.camera = vtkWidgetCamera(self.renderer)
        self.camera.SetInteractor(self.GetRenderWindow().GetInteractor())
        self.camera.EnabledOn()

        self.printer = vtkWidgetPrinter()
        self.printer.windowFilter.SetInput(self.GetRenderWindow())

        self.controller = vtkWidgetController(self)
        self.controller.SetDefaultRenderer(self.renderer)
        self.interactor = self.GetRenderWindow().GetInteractor()
        self.interactor.SetInteractorStyle(self.controller)
        self.interactor.Initialize()


    def load_lattice(self, vtklattice: vtkLattice):
        self.viewer.load_lattice(vtklattice)
        vtklattice.render(self.renderer)
        return self

    def close(self):
        self.Finalize()
        super().close()
