from vtkLattice import vtkLattice, vtkViewer


class QtViewerItem:
    def __init__(self, _parent):
        self._parent = _parent
        self._children = []
        self._data = []

    def VTKLatticeItem(self, lattice):
        if self._parent and isinstance(lattice, vtkLattice):
            self._vtk = lattice
            self._data = [lattice.name]

    def isVTKLatticeItem(self):
        return isinstance(self._vtk, vtkLattice)

    def VTKViewerItem(self, viewer):
        if self._parent and isinstance(viewer, vtkViewer):
            self._vtk = viewer
            self._data = [viewer.name]
            for lattice in viewer:
                latticeItem = QtViewerItem(self)
                latticeItem.VTKLatticeItem(lattice)
                self.append(latticeItem)

    def isVTKViewerItem(self):
        return isinstance(self._vtk, vtkViewer)

    def parent(self):
        return self._parent

    def children(self):
        return self._children

    def append(self, child):
        self._children.append(child)

    def child(self, row):
        return self._children[row]

    def data(self, column):
        return self._data[column]

    def dataCount(self):
        return self._data.__len__()

    def childCount(self):
        return self._children.__len__()

    def row(self):
        return self.parent().children().index(self)
