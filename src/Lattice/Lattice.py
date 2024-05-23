import numpy as np

from .LatticeBasis import LatticeBasis
from .LatticeAtoms import LatticeAtoms
from .LatticeBonds import LatticeBonds
from .LatticePolys import LatticePolys
from .LatticeSuper import LatticeSuper
from .LatticeSlab import LatticeSlab


class Lattice:

    def __init__(self,
                 name: str = "",
                 basis: LatticeBasis = None,
                 atoms: LatticeAtoms = None,
                 bonds: LatticeBonds = None,
                 polys: LatticePolys = None,
                 ):
        self.name = name
        if not basis is None and not isinstance(basis, LatticeBasis):
            basis = LatticeBasis(basis)
        self.basis = LatticeBasis() if basis is None else basis
        self.atoms = LatticeAtoms(basis=self.basis) if atoms is None else atoms
        self.bonds = LatticeBonds(basis=self.basis) if bonds is None else bonds
        self.polys = LatticePolys(basis=self.basis) if polys is None else polys

    def center(self):
        return np.sum(self.basis, axis=0) / 2

    def set_center(self, center):
        sites = self.atoms.sites() - np.array(center)
        self.atoms.set_sites(sites.centered())
        return self

    def set_origin(self, origin):
        sites = self.atoms.sites() - np.array(origin)
        self.atoms.set_sites(sites.periodic())
        return self

    def transform(self, matrix):
        print(matrix, np.linalg.det(matrix))
        if np.abs(np.linalg.det(matrix)) > 1:
            ncell = np.round(np.sum(np.abs(matrix), axis=1))
            print(ncell)
            super_cell = LatticeSuper(ncell)
            self.atoms = super_cell.make_atoms(self.atoms, self.basis)
            self.atoms.set_sites(self.atoms.sites()*ncell)
        self.basis = self.basis.transform(matrix)
        self.atoms = self.atoms.transform(matrix)
        self.bonds = LatticeBonds(basis=self.basis)
        self.polys = LatticePolys(basis=self.basis)
        return self

    def super_cell(self, index):
        super_cell = LatticeSuper(index)
        name = super_cell.make_name(self.name)
        basis = super_cell.make_basis(self.basis)
        atoms = super_cell.make_atoms(self.atoms, basis)
        return Lattice(name, basis, atoms)

    def slab_cell(self, index, axis):
        slab_cell = LatticeSlab(index, axis)
        name = slab_cell.make_name(self.name)
        basis = slab_cell.make_basis(self.basis)
        atoms = slab_cell.make_atoms(self.atoms, basis)
        return Lattice(name, basis, atoms)

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
            np.savetxt(poscar, self.basis.reduced(), fmt='%16.10f')
            np.savetxt(poscar, [list(self.atoms.count().keys())], fmt='%6s')
            np.savetxt(poscar, [list(self.atoms.count().values())], fmt='%6s')
            poscar.write('Direct\n')
            np.savetxt(poscar, self.atoms.sites(), fmt='%16.10f')
            return self
