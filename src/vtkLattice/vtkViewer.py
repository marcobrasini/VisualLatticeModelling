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

    def load_lattice(self, vtklattice: vtkLattice):
        self.lattice.append(vtklattice)
        return self

    def append(self, vtklattice: vtkLattice):
        self.lattice.append(vtklattice)
        return self
