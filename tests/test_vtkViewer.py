from src.vtkLattice.vtkViewer import vtkViewer
from src.vtkLattice.vtkLattice import vtkLattice
from . import Example, openqt


@openqt
def test_viewer():
    vtkviewer = vtkViewer()
    vtkviewer.name = "vtkViewer"
    vtkviewer.load_lattice(vtkLattice(Example.lattice))
    return vtkviewer
