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
        if isinstance(results, tuple):
            for result in results:
                result.render(renderer)
        else:
            results.render(renderer)

        renderWindow.Render()
        renderWindowInteractor.Start()

    return rendering


class Example:

    from Lattice import Lattice

    poscar = 'tests/example/poscar.vasp'
    lattice = Lattice().load_poscar(poscar)
    lattice.bonds = lattice.bonds.make(lattice.atoms['Zr'], lattice.atoms['O'], 2.5)
    lattice.bonds = lattice.bonds.make(lattice.atoms['Si'], lattice.atoms['O'], 2.5)
    lattice.polys = lattice.polys.make(lattice.atoms['Zr'], lattice.atoms['O'], 6)
    lattice.polys = lattice.polys.make(lattice.atoms['Si'], lattice.atoms['O'], 4)
