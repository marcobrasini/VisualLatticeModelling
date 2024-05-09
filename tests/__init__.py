# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def render(func):

    def rendering(*args, **kwargs):
        renderer = vtkRenderer()
        renderer.SetBackground((1.0, 1.0, 1.0))
        renderer.GetActiveCamera().ParallelProjectionOn()
        renderer.GetActiveCamera().SetPosition(0, 0, 1000)
        renderWindow = vtkRenderWindow()
        renderWindow.AddRenderer(renderer)
        renderWindowInteractor = vtkRenderWindowInteractor()
        renderWindowInteractor.SetRenderWindow(renderWindow)
        interactorStyle = vtkInteractorStyleTrackballCamera()
        renderWindowInteractor.SetInteractorStyle(interactorStyle)

        results = func(*args, **kwargs)
        renderer.AddActor(results.actor)

        renderWindow.Render()
        renderWindowInteractor.Start()

    return rendering

