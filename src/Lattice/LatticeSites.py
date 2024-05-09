import numpy as np
from .LatticeArray import LatticeArray


class LatticeSitesError(AttributeError):
    pass


class LatticeSites(LatticeArray):

    def periodic(self):
        basis = self.basis
        _sites = self.view(np.ndarray)
        while np.any(0.0 > _sites) or np.any(_sites >= 1.0):
            _sites = np.where(_sites < 0.0, _sites + 1.0, _sites)
            _sites = np.where(_sites >= 1.0, _sites - 1.0, _sites)
        self = _sites.view(type(self))
        self.basis = basis
        return self

    def centered(self):
        basis = self.basis
        _sites = self.view(np.ndarray)
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
