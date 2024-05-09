import numpy as np
import scipy as sp

from .LatticeAtoms import LatticeAtoms
from .LatticeAtom import LatticeAtom


DEFAULT_CENTER = np.zeros(3)


class LatticePoly:

    def __init__(self,
                 atoms: LatticeAtoms,
                 center: (LatticeAtom, np.ndarray) = DEFAULT_CENTER,
                 ):
        self.atoms = atoms
        self.center = center

    def hull(self):
        sites = self.atoms.sites() - self.center.site
        sites = sites.centered().cartesian()
        return sp.spatial.ConvexHull(sites)

    def volume(self):
        return self.hull().volume

    def area(self):
        return self.hull().area
