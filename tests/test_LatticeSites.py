import pytest
import numpy as np

from src.Lattice.LatticeSites import LatticeSites
from src.Lattice.LatticeSites import LatticeSitesError
from . import Example


class Test_LatticeSites:

    basis = Example.basis
    sites = Example.sites
    matrix = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [1 / 3, 1 / 3, 1 / 3],
    ])

    def test__init__(self):
        sites = LatticeSites(self.sites, basis = self.basis)
        assert np.array_equal(sites.basis, self.basis)
        assert np.array_equal(sites, self.sites)

    def test__init__default(self):
        sites = LatticeSites(self.sites)
        assert sites.basis is None
        assert np.array_equal(sites, self.sites)

    def test_set_basis(self):
        sites = LatticeSites(self.sites, basis = self.basis)
        positions = sites.cartesian()
        sites = sites.set_basis(self.matrix @ self.basis)
        assert isinstance(sites, LatticeSites)
        assert np.array_equal(sites.basis, self.matrix @ self.basis)
        assert np.allclose(sites.cartesian(), positions)

    def tests_transform(self):
        sites = LatticeSites(self.sites, basis = self.basis)
        positions = sites.cartesian()
        sites = sites.transform(self.matrix)
        assert isinstance(sites, LatticeSites)
        assert np.array_equal(sites.basis, self.matrix@self.basis)
        assert np.allclose(sites.cartesian(), positions)

    def test_periodic(self):
        sites = LatticeSites(self.sites + 1.0, basis=self.basis)
        sites = sites.periodic()
        assert isinstance(sites, LatticeSites)
        assert np.all(sites >= 0.0) and np.all(sites < 1.0)

    def test_periodic_multi(self):
        sites = LatticeSites(self.sites + 3.0, basis=self.basis)
        sites = sites.periodic()
        assert isinstance(sites, LatticeSites)
        assert np.all(sites >= 0.0) and np.all(sites < 1.0)

    def test_centered(self):
        sites = LatticeSites(self.sites, basis=self.basis)
        sites = sites.centered()
        assert isinstance(sites, LatticeSites)
        assert np.all(sites > -0.5) and np.all(sites <= 0.5)

    def test_centered_multi(self):
        sites = LatticeSites(self.sites+3, basis=self.basis)
        sites = sites.centered()
        assert isinstance(sites, LatticeSites)
        assert np.all(sites > -0.5) and np.all(sites <= 0.5)



    def test_cartesian(self):
        sites = LatticeSites(self.sites, basis=self.basis)
        assert np.array_equal(sites.cartesian(), self.sites @ self.basis)

    def test_cartesian_error(self):
        with pytest.raises(LatticeSitesError):
            sites = LatticeSites(self.sites)
            sites.cartesian()

    def test_norm(self):
        norms = np.linalg.norm(self.sites@self.basis, axis=1)
        sites = LatticeSites(self.sites, basis=self.basis)
        assert np.array_equal(sites.norm(), norms)

    def test_unique(self):
        sites = np.vstack((self.sites,self.sites, self.sites))
        sites = LatticeSites(sites, basis=self.basis)
        assert len(sites.unique()) == len(self.sites)
