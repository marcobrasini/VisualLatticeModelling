import numpy as np

from .LatticeAtom import LatticeAtom


class LatticeBond:

    atom1: LatticeAtom
    atom2: LatticeAtom

    def __init__(self,
                 atom1: LatticeAtom,
                 atom2: LatticeAtom,
                 ):
        self.atom1 = atom1
        self.atom2 = atom2

    def __eq__(self, other):
        return self.atom1 == other.atom1 and self.atom2 == other.atom2

    def vector(self):
        vector = self.atom2.site - self.atom1.site
        return vector.centered()

    def versor(self):
        vector = self.vector().cartesian()
        return vector/self.length()

    def center(self):
        vector = self.vector()
        return 0.5*vector + self.atom1.site

    def length(self):
        vector = self.vector().cartesian()
        return np.linalg.norm(vector)

    def image(self):
        image = np.zeros(3)
        vectors = self.atom2.site - self.atom1.site
        image = np.where(vectors <= -0.5, image+1, image)
        image = np.where(vectors > 0.5, image-1, image)
        return image
