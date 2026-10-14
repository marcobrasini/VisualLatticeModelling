import numpy as np
import scipy as sp
import itertools as it
from .LatticeAtoms import LatticeAtoms
from .LatticeAtom import LatticeAtom


DEFAULT_CENTER = np.zeros(3)


class LatticePoly:

    def __init__(self,
                 others: LatticeAtoms,
                 center: (LatticeAtom, np.ndarray) = DEFAULT_CENTER,
                 ):
        self.center = center
        self.others = others

    def atoms(self):
        atoms = self.others.append(self.center)
        atoms.basis = self.others.basis
        return atoms

    def hull(self):
        return sp.spatial.ConvexHull(self.points().cartesian())

    def points(self):
        sites = self.others.sites() - self.center.site
        return sites.centered()

    def vertices(self):
        return self.hull().vertices

    def simplices(self):
        return self.hull().simplices

    def volume(self):
        return self.hull().volume

    def area(self):
        return self.hull().area

    def ideal_length(self):
        if len(self.others) == 6:
            return (3*self.volume()/4)**(1/3)
        if len(self.others) == 4:
            return (9*np.sqrt(3)*self.volume()/8)**(1/3)

    def ideal_angle(self):
        if len(self.others) == 6:
            return 90
        if len(self.others) == 4:
            return 109.47

    def internal_angle(self):
        sites = self.others.sites() - self.center.site
        bonds = sites.centered()
        angles = []
        for i,j in it.combinations(range(len(self.others)), 2):
            angles.append(1-sp.spatial.distance.cosine(bonds[i], bonds[j]))
        angles = np.degrees(np.arccos(angles))
        return angles

    def internal_length(self):
        sites = self.others.sites() - self.center.site
        lengths = sites.centered().norm()
        return lengths

    def distortion_angle(self):
        angles = self.internal_angle()
        if len(self.others) == 6:
            angles = np.sort(angles)[:-3]
        # if len(self.others) == 4:
        #     angles = np.sort(angles)[:-2]
        angles = (angles - self.ideal_angle())**2
        return angles/(len(angles)-1)

    def distortion_length(self):
        lengths = self.internal_length() / self.ideal_length()
        return lengths**2/len(lengths)