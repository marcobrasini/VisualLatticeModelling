from copy import deepcopy

import numpy as np

from .LatticeArray import LatticeArray
from .LatticeSites import LatticeSites
from .LatticeSite import LatticeSite
from .LatticeAtom import LatticeAtom


class LatticeAtoms(LatticeArray):

    def __getitem__(self, item):
        if isinstance(item, str):
            item = self.atoms() == item
        return super().__getitem__(item)

    def copy(self):
        return deepcopy(self)

    def count(self):
        count = np.unique(self.atoms(), return_counts=True)
        return dict(zip(*count))

    def atoms(self):
        atoms = super().get_attribute('atom')
        return atoms

    def names(self):
        names = super().get_attribute('name')
        return names

    def sites(self):
        sites = super().get_attribute('site')
        return LatticeSites(sites, basis=self.basis)

    def vars(self):
        return super().get_attribute('var')

    def qs(self):
        return super().get_attribute('q')

    def set_atoms(self, atoms):
        super().set_attribute('atom', atoms)
        return self

    def set_names(self, names):
        super().set_attribute('name', names)
        return self

    def set_sites(self, sites):
        sites = [LatticeSite(site, self.basis) for site in sites]
        super().set_attribute('site', sites)
        return self

    def set_vars(self, vars):
        super().set_attribute('var', vars)
        return self

    def set_qs(self, qs):
        super().set_attribute('q', qs)
        return self

    def set_basis(self, basis):
        sites = self.sites().set_basis(basis)
        self.set_sites(sites)
        self.basis = basis
        return self

    def periodic(self):
        self.set_sites(self.sites().periodic())
        return self

    def unique(self, tollerance=6):
        index = self.sites().periodic().unique(tollerance)
        self = self.take(index)
        return self

    def transform(self, matrix):
        self = self.set_basis(matrix @ self.basis)
        self = self.periodic()
        self = self.unique()
        return self

    def make(self,
             atoms: list,
             names: list = None,
             sites: list = None,
             vars: list = None,
             qs: list = None):
        basis = self.basis
        _atoms = []
        for i, atom in enumerate(atoms):
            name = None if names is None else names[i]
            site = None if sites is None else LatticeSite(sites[i], basis)
            var = None if vars is None else vars[i]
            q = None if qs is None else qs[i]
            _atoms.append(LatticeAtom(atom, name, site , var, q))
        self = np.append(self, _atoms).view(LatticeAtoms)
        self.basis = basis
        return self

    def make_vars(self, atoms):
        delta = self.sites() - atoms.sites()
        basis = atoms.basis
        sites = atoms.sites()
        sites = np.where(delta <= -0.5, sites - 1, sites)
        sites = np.where(delta > +0.5, sites + 1, sites)
        vars = self.sites().cartesian() - sites @ basis
        self.set_vars(vars)
        return self