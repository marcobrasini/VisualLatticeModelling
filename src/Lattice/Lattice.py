import numpy as np
# from tqdm import tqdm

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

    def set_basis(self, basis, parameter=1.0):
        self.basis = LatticeBasis(basis, parameter)
        self.atoms.basis = self.basis
        for atom in self.atoms:
            atom.site.basis = self.basis
        self.bonds.basis = self.basis
        self.polys.basis = self.basis

    def center(self):
        return np.sum(self.basis, axis=0) / 2

    def set_center(self, center):
        sites = self.atoms.sites() + (0.5 - np.array(center))
        self.atoms.set_sites(sites.centered())
        return self

    def set_origin(self, origin):
        sites = self.atoms.sites() - np.array(origin)
        self.atoms.set_sites(sites.periodic())
        return self

    def transform(self, matrix):
        if np.abs(np.linalg.det(matrix)) > 1:
            ncell = np.round(np.sum(np.abs(matrix), axis=1))
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

    def madelung(self, atom, n, charge, atoms = None):
        n = n if hasattr(n, "__len__") else [n]*3
        index = self.atoms.index(atom)
        if not atoms is None:
            subcell = Lattice('', self.basis, atoms)
            superlattice = subcell.super_cell([2 * i + 1 for i in n])
        else:
            superlattice = self.super_cell([2 * i + 1 for i in n])
        sites = superlattice.atoms.sites()
        atoms = superlattice.atoms.atoms()
        site0 = sites[index]
        sites = np.delete(sites, index, axis=0)
        atoms = np.delete(atoms, self.atoms.index(atom))
        delta = (sites - site0).centered().cartesian()
        charges = np.array([charge[atom] for atom in atoms])
        return np.sum(charges / np.linalg.norm(delta, axis=1))

    @classmethod
    def load_poscar(cls, poscar):
        with open(poscar, 'r') as poscar:
            name = poscar.readline().strip()
            parameter = float(poscar.readline())
            basis = np.loadtxt(poscar, float, skiprows=0, max_rows=3)
            atoms = np.repeat(np.loadtxt(poscar, str, max_rows=1),
                              np.loadtxt(poscar, int, max_rows=1))
            sites = np.loadtxt(poscar, float, skiprows=1, max_rows=len(atoms))
            basis = LatticeBasis(basis, parameter=parameter)
            atoms = LatticeAtoms(basis=basis).make(atoms, sites=sites)
            return cls(name, basis, atoms)

    def save_poscar(self, poscar, selective=None):
        with open(poscar, 'w') as poscar:
            poscar.write(self.name + '\n')
            poscar.write('{:.10f}\n'.format(self.basis.parameter))
            np.savetxt(poscar, self.basis.reduced(), fmt='%16.10f')
            atoms = self.atoms.count()
            np.savetxt(poscar, [[atom for atom in atoms.keys() if atom]], fmt='%6s')
            np.savetxt(poscar, [[atoms[atom] for atom in atoms.keys() if atom]], fmt='%6s')
            if selective is None:
                poscar.write('Direct\n')
                for atom in self.atoms.count().keys():
                    if atom == '':
                        continue
                    sites = self.atoms[atom].sites()
                    np.savetxt(poscar, sites, fmt='%16.10f')
            else:
                poscar.write('Selective dynamics\n')
                poscar.write('Direct\n')
                for atom in self.atoms.count().keys():
                    if atom == '':
                        continue
                    sites = self.atoms[atom].sites()
                    selection = selective[self.atoms.atoms()==atom]
                    selection = selection.astype(str)
                    sites = np.hstack((sites, selection), dtype=object)
                    np.savetxt(poscar, sites, fmt=[*['%16.10f']*3, *['%6s']*3])
            return self

    @classmethod
    def copy(cls, lattice):
        import copy
        lattice_copy = cls()
        lattice_copy.name = copy.deepcopy(lattice.name)
        lattice_copy.basis = copy.deepcopy(lattice.basis)
        lattice_copy.atoms = copy.deepcopy(lattice.atoms)
        return lattice_copy
