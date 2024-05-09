from vtkmodules.vtkFiltersCore import vtkAppendPolyData
from vtkmodules.vtkCommonDataModel import vtkPolyData
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkRenderingCore import vtkGlyph3DMapper, vtkPolyDataMapper, vtkActor
from Lattice import LatticeAtom
from .vtkLatticePeriodicTable import default_radius, default_color
from .lib.vtkSourceSphere import vtkSourceSphere
from .lib.vtkSourceArrow import vtkSourceArrow
from .lib.vtkEntity import vtkEntity


DEFAULT_RESOLUTION = 12


class vtkLatticeAtomSource(vtkAppendPolyData):

    def __init__(self, atom: LatticeAtom):
        vtkAppendPolyData.__init__(self)
        self.sphere = vtkSourceSphere()
        self.sphere.set_center(atom.site.cartesian())
        self.sphere.set_radius(default_radius(atom.atom))
        self.sphere.set_resolution(DEFAULT_RESOLUTION)
        self.arrow = vtkSourceArrow()
        self.arrow.set_vector(atom.var)
        self.arrow.set_origin(atom.site.cartesian())
        self.arrow.set_resolution(DEFAULT_RESOLUTION)
        self.AddInputConnection(self.sphere.GetOutputPort())
        self.AddInputConnection(self.arrow.GetOutputPort())

    def draw(self, sphere, arrow):
        self.RemoveAllInputConnections(0)
        if sphere: self.AddInputConnection(self.sphere.GetOutputPort())
        if arrow: self.AddInputConnection(self.arrow.GetOutputPort())


class vtkLatticeAtom(vtkEntity):

    def __init__(self,
                 atom: LatticeAtom,
                 image: list = [[0, 0, 0]],
                 ):
        self.atom = atom
        self.image = list(image)
        self.source = vtkLatticeAtomSource(self.atom)
        self.mapper = vtkGlyph3DMapper()
        self.mapper.SetSourceConnection(self.source.GetOutputPort())
        self.actor = vtkActor()
        self.actor.SetMapper(self.mapper)
        self.set_color(default_color(atom.atom))
        self.set_image()

    def color(self):
        return self.actor.GetProperty().GetColor()

    def set_color(self, color):
        self.actor.GetProperty().SetColor(color)
        return self

    def set_image(self, image=None):
        if not image is None: self.image = list(image)
        points = vtkPoints()
        for cell in self.image:
            point = cell @ self.atom.site.basis
            points.InsertNextPoint(point)
        datapoints = vtkPolyData()
        datapoints.SetPoints(points)
        self.mapper.RemoveAllInputs()
        self.mapper.SetInputData(datapoints)
        return self

    def add_image(self, image):
        self.image.append(list(image))
        self.set_image()
