from vtkLattice import vtkLattice, vtkViewer



class QtViewerItem:

    VTKRootItem = 0
    VTKViewerItem = 1
    VTKLatticeItem = 2

    def __init__(self, _parent):
        self._parent = _parent
        self._children = []
        self._data = []

    def setVTKLatticeItem(self, lattice = None):
        if lattice is None:
            self._vtk = QtViewerItem.VTKLatticeItem
            return self
        # if self._parent and isinstance(lattice, vtkLattice):
        self._vtk = lattice
        self._data = [lattice.name]
        return self

    def setVTKViewerItem(self, viewer = None):
        if viewer is None:
            self._vtk = QtViewerItem.VTKLatticeItem
            return self
        # if self._parent and isinstance(viewer, vtkViewer):
        self._vtk = viewer
        self._data = [viewer.name]
        for lattice in viewer:
            latticeItem = QtViewerItem(self)
            latticeItem.setVTKLatticeItem(lattice)
            self.append(latticeItem)
        return self

    def isVTKRootItem(self):
        return self._vtk is None or self._vtk == self.VTKRootItem

    def isVTKViewerItem(self):
        return isinstance(self._vtk, vtkViewer) or self._vtk == self.VTKViewerItem

    def isVTKLatticeItem(self):
        return isinstance(self._vtk, vtkLattice) or self._vtk == self.VTKLatticeItem

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

    def setData(self, data):
        if data:
            self._vtk.name = data
            self._data = [data]

    def dataCount(self):
        return self._data.__len__()

    def childCount(self):
        return self._children.__len__()

    def row(self):
        return self.parent().children().index(self)

    def insertChild(self, index, child):
        if 0 <= index <= len(self._children):
            child._parent = self
            self._children.insert(index, child)
            return True
        return False

    def removeChild(self, index):
        if 0 <= index < len(self._children):
            del self._children[index]
            return True
        return False
