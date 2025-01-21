from vtkmodules.vtkFiltersCore import vtkAppendPolyData
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper
from Lattice import LatticeAtom
from .lib.vtkBatch import vtkBatch
from .lib.vtkImage import vtkImage
from .lib.vtkSourceSphere import vtkSourceSphere
from .lib.vtkSourceArrow import vtkSourceArrow
from .vtkPeriodicTable import default_radius, default_color


DEFAULT_RESOLUTION = 12


class vtkLatticeAtomSource(vtkAppendPolyData):

    def __init__(self, atom: LatticeAtom):
        vtkAppendPolyData.__init__(self)
        self.sphere = vtkSourceSphere()
        self.sphere.set_radius(default_radius(atom.atom))
        self.sphere.set_resolution(DEFAULT_RESOLUTION)
        self.arrow = vtkSourceArrow()
        self.arrow.set_resolution(DEFAULT_RESOLUTION)
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
            self.AddInputConnection(self.sphere.GetOutputPort())
        if arrow:
            self.AddInputConnection(self.arrow.GetOutputPort())
        if invert:
            self.arrow.source.SetInvert(invert)
            self.arrow.set_vector(-self.variation)


class vtkLatticeAtom(vtkBatch):
    def __init__(self,
                 atom: LatticeAtom,
                 images: list = [[0, 0, 0]],
                 ):
        super().__init__()
        self.atom = atom
        self.source = vtkLatticeAtomSource(self.atom)
        self.color = default_color(self.atom.atom)
        self.set_images(images)
        self.draw(True, True)

    def new_image(self, image):
        image = (self.atom.site + image).cartesian()
        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(self.source.GetOutputPort())
        return vtkImage(self, mapper, image).set_color(self.color)

    def draw(self, sphere=True, arrow=True, invert=False):
        self.source.draw(sphere, arrow, invert)
