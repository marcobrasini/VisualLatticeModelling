from vtkmodules.vtkIOImage import vtkPNGWriter
from vtkmodules.vtkRenderingCore import vtkWindowToImageFilter


class vtkWidgetPrinter(vtkPNGWriter):

    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.windowFilter = vtkWindowToImageFilter()

        self.windowFilter.ReadFrontBufferOff()
        self.windowFilter.SetInput(self.widget.GetRenderWindow())
        self.SetInputConnection(self.windowFilter.GetOutputPort())

    def print(self, name, resolution=4, transparent=True):
        if transparent:
            self.windowFilter.SetInputBufferTypeToRGBA()
        else:
            self.windowFilter.SetInputBufferTypeToRGB()
        self.SetFileName(name + '.png')
        self.windowFilter.SetScale(resolution)
        self.windowFilter.SetInput(self.widget.GetRenderWindow())
        self.SetInputConnection(self.windowFilter.GetOutputPort())
        self.windowFilter.Modified()
        self.windowFilter.Update()
        self.Write()
