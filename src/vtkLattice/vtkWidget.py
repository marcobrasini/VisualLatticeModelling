from PyQt5.QtWidgets import QWidget
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkRenderingCore import vtkRenderer
from .vtkLattice import vtkLattice
from .vtkWidgetInteractor import vtkWidgetInteractor
from .vtkWidgetCamera import vtkWidgetCamera
from .vtkWidgetPicker import vtkWidgetPicker
from .vtkWidgetDrawer import vtkWidgetDrawer
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
        self.GetRenderWindow().SetAlphaBitPlanes(1)
        self.GetRenderWindow().AddRenderer(vtkRenderer())
        self.renderer().SetBackground((1.0, 1.0, 1.0))
        self.renderer().ResetCamera()
        self.renderer().GetActiveCamera().ParallelProjectionOn()
        self.renderer().GetActiveCamera().SetPosition(0, 0, 1000)

        self.camera = vtkWidgetCamera(self, camera)
        self.picker = vtkWidgetPicker(self)
        self.drawer = vtkWidgetDrawer(self)
        self.printer = vtkWidgetPrinter(self)

        self.interactor().SetInteractorStyle(vtkWidgetInteractor(self))
        self.interactor().Initialize()
        self.interactor().Start()
        self.render()

    def window(self):
        return self.GetRenderWindow()

    def renderer(self):
        return self.GetRenderWindow().GetRenderers().GetFirstRenderer()

    def interactor(self):
        return self.GetRenderWindow().GetInteractor()

    def controller(self):
        return self.interactor().GetInteractorStyle()

    def name(self):
        return self.viewer.name

    def setName(self, name: str):
        self.viewer.name = name

    def lattice(self, i: int):
        return self.viewer.lattice[i]

    def renderLattice(self, vtklattice: vtkLattice):
        vtklattice.render(self.renderer())

    def deleteLattice(self, vtklattice: vtkLattice):
        vtklattice.delete(self.renderer())

    def appendLattice(self, vtklattice: vtkLattice):
        self.viewer.appendLattice(vtklattice)
        self.renderLattice(vtklattice)
        return self

    def insertLattice(self, vtklattice: vtkLattice, index: int):
        self.viewer.insertLattice(vtklattice, index)
        self.renderLattice(vtklattice)

    def removeLattice(self, index):
        self.deleteLattice(self.viewer[index])
        self.viewer.removeLattice(index)

    def render(self):
        for lattice in self.viewer:
            lattice.render(self.renderer())
        return self

    def delete(self):
        for lattice in self.viewer:
            lattice.delete(self.renderer)

    def refresh(self):
        self.renderer.GetRenderWindow().Render()

    def close(self):
        self.Finalize()
        super().close()

    def openPicker(self, picker):
        self.controller().picker = picker

    def closePicker(self):
        self.controller().escape()

    def print(self):
        self.printer.print(self.name())