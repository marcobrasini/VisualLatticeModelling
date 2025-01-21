from .lib.vtkGroup import vtkGroup
from .lib.vtkEntityArrow import vtkEntityArrow
from .lib.vtkEntitySphere import vtkEntitySphere

DEFAULT_RATIO = 0.2
DEFAULT_RADIUS = 0.2
DEFAULT_RESOLUTION = 12


class vtkLatticeBasis(vtkGroup):

    def __init__(self, basis):
        super().__init__()
        self.basis = basis
        self.O = vtkEntitySphere().set_center((0., 0., 0.))
        self.a = vtkEntityArrow().set_vector(self.basis[0]).set_color((1., 0., 0.))
        self.b = vtkEntityArrow().set_vector(self.basis[1]).set_color((0., 1., 0.))
        self.c = vtkEntityArrow().set_vector(self.basis[2]).set_color((0., 0., 1.))
        self.set_ratio(DEFAULT_RATIO)
        self.set_radius(DEFAULT_RADIUS)
        self.set_resolution(DEFAULT_RESOLUTION)
        self.AddPart(self.O)
        self.AddPart(self.a)
        self.AddPart(self.b)
        self.AddPart(self.c)

    def set_ratio(self, ratio):
        length = [self.a.length(), self.b.length(), self.c.length()]
        tip = min([ratio * l for l in length])
        self.a.source.set_ratio(tip / length[0])
        self.b.source.set_ratio(tip / length[1])
        self.c.source.set_ratio(tip / length[2])

    def set_radius(self, radius):
        self.O.source.set_radius(2*radius)
        self.a.source.set_radius(radius)
        self.b.source.set_radius(radius)
        self.c.source.set_radius(radius)

    def set_resolution(self, resolution):
        self.O.source.set_resolution(resolution)
        self.a.source.set_resolution(resolution)
        self.b.source.set_resolution(resolution)
        self.c.source.set_resolution(resolution)

