from src.vtkLattice.vtkWidget import vtkWidget
from src.vtkLattice.vtkViewer import vtkViewer
from src.vtkLattice.vtkLattice import vtkLattice
from . import Example, openqt


@openqt
def test_widget():
    vtkviewer = vtkViewer()
    vtkwidget = vtkWidget(vtkviewer)
    vtkwidget.appendLattice(vtkLattice(Example.lattice()))
    assert vtkwidget.parent() is None
    return vtkwidget
