import numpy as np
from .LatticeSite import LatticeSite


class LatticeAtom:

    atom: str
    name: str
    site: LatticeSite
    var: np.ndarray

    def __init__(self,
                 atom: str = '',
                 name: str = None,
                 site: LatticeSite = None,
                 var: np.ndarray = None):
        self.atom = atom
        self.name = atom if name is None else name
        self.site = site if isinstance(site, LatticeSite) else LatticeSite(site)
        self.var = np.zeros(3) if var is None else var

    def __eq__(self, other):
        return (self.atom == other.atom
                and self.name == other.name
                and self.site == other.site
                and np.array_equal(self.var, other.var))
