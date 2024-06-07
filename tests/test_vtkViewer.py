from src.vtkLattice.vtkViewer import vtkViewer
from src.vtkLattice.vtkLattice import vtkLattice
from . import Example


class Test_vtkViewer:

    lattice = Example.lattice

    def test_vtkViewer(self):
        vtkviewer = vtkViewer("vtkViewer")
        vtkviewer.load_lattice(vtkLattice(self.lattice))
        assert vtkviewer.name == "vtkViewer"
