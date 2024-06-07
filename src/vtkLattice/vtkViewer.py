from vtkmodules.vtkRenderingCore import vtkRenderer
from .vtkLattice import vtkLattice


class vtkViewer:

    def __init__(self,
                 name: str = None,
                 ):
        self.name = name or ""
        self.lattice = []

    def __len__(self):
        return self.lattice.__len__()

    def __iter__(self):
        return self.lattice.__iter__()

    def __getitem__(self, item):
        return self.lattice.__getitem__(item)

    def appendLattice(self, vtklattice: vtkLattice):
        self.lattice.append(vtklattice)
        return self

    def insertLattice(self, vtklattice: vtkLattice, index: int):
        self.lattice.insert(index, vtklattice)

    def removeLattice(self, index):
        del self.lattice[index]

    def render(self, renderer: vtkRenderer):
        for lattice in self.lattice:
            lattice.render(renderer)
