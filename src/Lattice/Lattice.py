from .LatticeBasis import LatticeBasis
from .LatticeAtoms import LatticeAtoms
from .LatticeBonds import LatticeBonds
from .LatticePolys import LatticePolys


class Lattice:

    def __init__(self,
                 name: str = "",
                 basis: LatticeBasis = None,
                 atoms: LatticeAtoms = None,
                 bonds: LatticeBonds = None,
                 polys: LatticePolys = None,
                 ):
        self.name = name
        self.basis = basis
        self.atoms = atoms
        self.bonds = bonds
        self.polys = polys



