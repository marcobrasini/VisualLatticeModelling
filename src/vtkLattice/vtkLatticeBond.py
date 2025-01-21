import numpy as np
from vtkmodules.vtkFiltersCore import vtkElevationFilter
from vtkmodules.vtkRenderingCore import vtkDiscretizableColorTransferFunction
from vtkmodules.vtkRenderingCore import vtkPolyDataMapper, vtkActor
from Lattice import LatticeBond
from .lib.vtkBatch import vtkBatch
from .lib.vtkImage import vtkImage
from .lib.vtkSource import vtkSource
from .lib.vtkSourceCylinder import vtkSourceCylinder
from .vtkLatticeAtoms import vtkLatticeAtoms


DEFAULT_RADIUS = 0.1
DEFAULT_RESOLUTION = 12


class vtkLatticeBondSource(vtkSource):
    def __init__(self, bond: LatticeBond):
        super().__init__()
        self.cylinder = vtkSourceCylinder()
        self.cylinder.set_radius(DEFAULT_RADIUS)
        self.cylinder.set_resolution(DEFAULT_RESOLUTION)
        self.filter = vtkElevationFilter()
        self.filter.SetInputConnection(self.cylinder.GetOutputPort())
        self.filter.SetScalarRange(-1, 1)
        self.filter.SetLowPoint(0, -1, 0)
        self.filter.SetHighPoint(0, 1, 0)
        self.SetInputConnection(self.filter.GetOutputPort())
        self.rescale((1.0, bond.length(), 1.0))
        self.orientate(bond.versor(), axis=1)


class vtkLatticeBondColor(vtkDiscretizableColorTransferFunction):
    def __init__(self,
                 colors,
                 interval = [-1, 1],
                 ):
        super().__init__()
        self.DiscretizeOn()
        self.SetScaleToLinear()
        self.SetNumberOfValues(len(colors))
        for x, color in zip(np.linspace(*interval, len(colors)), colors):
            self.AddRGBPoint(x, *color)


class vtkLatticeBond(vtkBatch):
    def __init__(self,
                 bond: LatticeBond,
                 vtkAtoms: vtkLatticeAtoms,
                 images: list = [[0, 0, 0]],
                 ):
        self.bond = bond
        self.atom1 = vtkAtoms[vtkAtoms.index(bond.atom1)]
        self.atom2 = vtkAtoms[vtkAtoms.index(bond.atom2)]
        self.colors = vtkLatticeBondColor([self.atom1.color, self.atom2.color])
        self.source = vtkLatticeBondSource(self.bond)
        self.set_images(images)
        self.draw(True, False)

    def new_image(self, image):
        image = (self.bond.center() + image).cartesian()
        mapper = vtkPolyDataMapper()
        mapper.SetInputConnection(self.source.GetOutputPort())
        mapper.SetLookupTable(self.colors)
        mapper.InterpolateScalarsBeforeMappingOn()
        return vtkImage(self, mapper, image)

    def set_color(self, color):
        self.colors = vtkLatticeBondColor([color, color])
        for image in self:
            image.mapper.SetLookupTable(self.colors)
        self.draw(True, False)

    def draw(self, image2, image1):
        image = self.bond.image()
        if not np.all(image == 0):
            if image2: self.atom2.add_image(+image)
            if image1: self.atom1.add_image(-image)
