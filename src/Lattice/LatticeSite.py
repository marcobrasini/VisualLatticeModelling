import numpy as np

from .LatticeSites import LatticeSites


class LatticeSite(LatticeSites):

    def __new__(cls,
                site: np.ndarray = None,
                basis: np.ndarray = None):
        if site is None:
            site = np.array([np.nan, np.nan, np.nan])
        return LatticeSites.__new__(cls, site, basis)

    def __eq__(self, other):
        return (np.array_equal(self, other, equal_nan=True)
                and np.array_equal(self.basis, other.basis))
