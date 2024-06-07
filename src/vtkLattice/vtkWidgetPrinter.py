from vtkmodules.vtkIOImage import vtkPNGWriter
from vtkmodules.vtkRenderingCore import vtkWindowToImageFilter


class vtkWidgetPrinter(vtkPNGWriter):

    def __init__(self):
        super().__init__()
        self.windowFilter = vtkWindowToImageFilter()
        self.windowFilter.SetInputBufferTypeToRGB()
        self.windowFilter.ReadFrontBufferOff()
        self.SetInputConnection(self.windowFilter.GetOutputPort())

    def print(self, name):
        self.SetFileName(name + '.png')
        self.windowFilter.Modified()
        self.windowFilter.Update()
        self.Write()
