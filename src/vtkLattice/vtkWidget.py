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
                 viewer: vtkViewer = None,
                 parent: QWidget = None,
                 camera: tuple = None,
                 ):
        super().__init__(parent=parent)
        self.viewer = viewer
        self.renderer = vtkRenderer()
        self.renderer.SetBackground((1.0, 1.0, 1.0))
        self.renderer.ResetCamera()
        self.renderer.GetActiveCamera().ParallelProjectionOn()
        self.renderer.GetActiveCamera().SetPosition(0, 0, 1000)
        self.GetRenderWindow().AddRenderer(self.renderer)

        self.camera = vtkWidgetCamera(self, camera)
        self.printer = vtkWidgetPrinter(self)

        self.controller = vtkWidgetController(self)
        self.controller.SetDefaultRenderer(self.renderer)
        self.interactor = self.GetRenderWindow().GetInteractor()
        self.interactor.SetInteractorStyle(self.controller)
        self.interactor.Initialize()

    def name(self):
        return self.viewer.name

    def setName(self, name):
        self.viewer.name = name

    def renderLattice(self, vtklattice: vtkLattice):
        vtklattice.render(self.renderer)

    def deleteLattice(self, vtklattice: vtkLattice):
        vtklattice.delete(self.renderer)

    def appendLattice(self, vtklattice: vtkLattice):
        self.viewer.appendLattice(vtklattice)
        self.renderLattice(vtklattice)

    def insertLattice(self, vtklattice: vtkLattice, index: int):
        self.viewer.insertLattice(vtklattice, index)
        self.renderLattice(vtklattice)

    def removeLattice(self, index):
        self.deleteLattice(self.viewer[index])
        self.viewer.removeLattice(index)

    def render(self):
        for lattice in self.viewer:
            lattice.render(self.renderer)

    def delete(self):
        for lattice in self.viewer:
            lattice.delete(self.renderer)

    def close(self):
        self.Finalize()
        super().close()
