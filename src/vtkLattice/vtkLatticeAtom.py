from vtkmodules.vtkFiltersCore import vtkAppendPolyData
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkRenderingCore import vtkGlyph3DMapper, vtkPolyDataMapper, vtkActor
from Lattice import LatticeAtom
from .vtkLatticePeriodicTable import default_radius, default_color
from .lib.vtkSourceSphere import vtkSourceSphere
from .lib.vtkSourceArrow import vtkSourceArrow
from .lib.vtkEntity import vtkEntity
from .lib.vtkArray import vtkArray


DEFAULT_RESOLUTION = 12


class vtkLatticeAtomSource(vtkAppendPolyData):

    def __init__(self, atom: LatticeAtom, image: list):
        vtkAppendPolyData.__init__(self)
        self.sphere = vtkSourceSphere()
        self.sphere.set_radius(default_radius(atom.atom))
        self.sphere.set_resolution(DEFAULT_RESOLUTION)
        self.arrow = vtkSourceArrow()
        self.arrow.set_vector(atom.var)
        self.arrow.set_resolution(DEFAULT_RESOLUTION)
        self.set_position((atom.site + image).cartesian())
        self.AddInputConnection(self.sphere.GetOutputPort())
        self.AddInputConnection(self.arrow.GetOutputPort())

    def set_position(self, position):
        self.sphere.set_center(position)
        self.arrow.set_origin(position)
        return self

    def draw(self, sphere, arrow):
        self.RemoveAllInputConnections(0)
        if sphere: self.AddInputConnection(self.sphere.GetOutputPort())
        if arrow: self.AddInputConnection(self.arrow.GetOutputPort())


class vtkLatticeAtomEntity(vtkEntity):

    def __init__(self,
                 atom: LatticeAtom,
                 image: list = [0, 0, 0],
                 ):
        self.source = vtkLatticeAtomSource(atom, image)
        self.mapper = vtkPolyDataMapper()
        self.mapper.SetInputConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)

    def color(self):
        return self.actor.GetProperty().GetColor()

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self


class vtkLatticeAtom(vtkArray):
    def __init__(self,
                 atom: LatticeAtom,
                 image: list = [[0, 0, 0]],
                 ):
        super().__init__([])
        self.atom = atom
        self.set_image(image)
        self.set_color(default_color(self.atom.atom))

    def draw(self, sphere, arrow):
        for atom in self:
            atom.source.draw(sphere, arrow)

    def set_image(self, image):
        self.image = image
        self.array = [vtkLatticeAtomEntity(self.atom, image) for image in self.image]
        return self

    def add_image(self, image):
        vtkatom = vtkLatticeAtomEntity(self.atom, image).set_color(self.color())
        self.array.append(vtkatom)
        return self

    def color(self):
        return self.array[0].color()

    def set_color(self, color):
        for atom in self:
            atom.set_color(color)
