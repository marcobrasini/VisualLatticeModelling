from vtkmodules.vtkFiltersCore import vtkAppendPolyData
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkRenderingCore import vtkGlyph3DMapper, vtkPolyDataMapper, vtkActor
from Lattice import LatticeAtom
from .vtkPeriodicTable import default_radius, default_color
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
        self.arrow.set_resolution(DEFAULT_RESOLUTION)
        self.set_position((atom.site + image).cartesian())
        self.set_variation(atom.var)
        self.AddInputConnection(self.sphere.GetOutputPort())
        self.AddInputConnection(self.arrow.GetOutputPort())

    def set_position(self, position):
        self.position = position
        self.sphere.set_center(self.position)
        self.arrow.set_origin(self.position)
        return self

    def set_variation(self, variation):
        self.variation = variation
        self.arrow.set_vector(self.variation)

    def draw(self, sphere=True, arrow=True, invert=False):
        self.RemoveAllInputConnections(0)
        if sphere:
            radius = self.sphere.radius()
            self.sphere = vtkSourceSphere()
            self.sphere.set_radius(radius)
            self.sphere.set_resolution(DEFAULT_RESOLUTION)
            self.AddInputConnection(self.sphere.GetOutputPort())
        if arrow:
            self.arrow = vtkSourceArrow()
            self.arrow.set_resolution(DEFAULT_RESOLUTION)
            self.AddInputConnection(self.arrow.GetOutputPort())
        self.set_position(self.position)
        self.set_variation(self.variation)
        if invert:
            self.arrow.source.SetInvert(invert)
            self.arrow.set_vector(-self.variation)


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
        self.source.draw()

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
        self.color = default_color(self.atom.atom)
        self.set_image(image)

    def draw(self, sphere=True, arrow=True, invert=False):
        for atom in self:
            atom.source.draw(sphere, arrow, invert)
            atom.source.Update()
            atom.mapper.Update()

    def set_image(self, image):
        self.image = image
        self.array = [vtkLatticeAtomEntity(self.atom, image) for image in self.image]
        self.set_color(self.color)
        return self

    def add_image(self, image):
        vtkatom = vtkLatticeAtomEntity(self.atom, image).set_color(self.color)
        self.array.append(vtkatom)
        return self

    def set_color(self, color):
        self.color = color
        for atom in self:
            atom.set_color(self.color)
