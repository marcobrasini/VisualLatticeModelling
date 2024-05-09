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
        return sp.spatial.ConvexHull(self.atoms.sites().cartesian())

    def volume(self):
        return self.hull().volume

    def area(self):
        return self.hull().area
