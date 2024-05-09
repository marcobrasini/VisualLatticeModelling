import numpy as np

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
        self.basis = LatticeBasis() if basis is None else basis
        self.atoms = LatticeAtoms(basis=self.basis) if atoms is None else atoms
        self.bonds = LatticeBonds(basis=self.basis) if bonds is None else bonds
        self.polys = LatticePolys(basis=self.basis) if polys is None else polys



    def load_poscar(self, poscar):
        with open(poscar, 'r') as poscar:
            name = poscar.readline().strip()
            parameter = float(poscar.readline())
            basis = np.loadtxt(poscar, float, skiprows=0, max_rows=3)
            atoms = np.repeat(np.loadtxt(poscar, str, max_rows=1),
                              np.loadtxt(poscar, int, max_rows=1))
            sites = np.loadtxt(poscar, float, skiprows=1, max_rows=len(atoms))
            basis = LatticeBasis(basis, parameter=parameter)
            atoms = LatticeAtoms(basis=basis).make(atoms, sites=sites)
            return Lattice(name, basis, atoms)

    def save_poscar(self, poscar):
        with open(poscar, 'w') as poscar:
            poscar.write(self.name + '\n')
            poscar.write('{:.10f}\n'.format(self.basis.parameter))
            np.savetxt(poscar, self.basis, fmt='%16.10f')
            np.savetxt(poscar, [list(self.atoms.count().keys())], fmt='%6s')
            np.savetxt(poscar, [list(self.atoms.count().values())], fmt='%6s')
            poscar.write('Direct\n')
            np.savetxt(poscar, self.atoms.sites(), fmt='%16.10f')
            return self
