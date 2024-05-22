import numpy as np
from .LatticeArray import LatticeArray


SITES_RESOLUTION = 10
SITES_TOLLERANCE = 1e-10


class LatticeSitesError(AttributeError):
    pass


class LatticeSites(LatticeArray):

    def __init__(self,
                 array: list = [],
                 basis: np.ndarray = None):
        self = np.round(self, SITES_RESOLUTION).view(LatticeSites)
        self.basis = basis

    def set_basis(self, basis):
        sites = self.cartesian() @ np.linalg.inv(basis)
        self = np.round(sites, SITES_RESOLUTION).view(type(self))
        self.basis = basis
        return self

    def transform(self, matrix):
        self = self.set_basis(matrix @ self.basis)
        return self

    def periodic(self):
        basis = self.basis
        _sites = np.round(self, SITES_RESOLUTION)
        while np.any(0.0 > _sites) or np.any(_sites >= 1.0):
            _sites = np.where(_sites < 0.0, _sites + 1.0, _sites)
            _sites = np.where(_sites >= 1.0, _sites - 1.0, _sites)
        self = _sites.view(type(self))
        self.basis = basis
        return self

    def centered(self):
        basis = self.basis
        _sites = np.round(self, SITES_RESOLUTION)
        while np.any(-0.5 >= _sites) or np.any(_sites > 0.5):
            _sites = np.where(_sites <= -0.5, _sites + 1.0, _sites)
            _sites = np.where(_sites > 0.5, _sites - 1.0, _sites)
        self = _sites.view(type(self))
        self.basis = basis
        return self

    def cartesian(self):
        if self.basis is None:
            raise LatticeSitesError
        return self.view(np.ndarray) @ self.basis

    def norm(self):
        return np.linalg.norm(self.cartesian(), axis=-1)

    def unique(self, resolution=SITES_RESOLUTION):
        sites = np.round(self, resolution)
        sites, index = np.unique(sites, return_index=True, axis=0)
        return index
