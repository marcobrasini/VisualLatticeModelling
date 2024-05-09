import numpy as np
from src.Lattice.LatticeSite import LatticeSite
from src.Lattice.LatticeSites import LatticeSites
from src.Lattice.LatticeAtom import LatticeAtom
from src.Lattice.LatticeAtoms import LatticeAtoms
from src.Lattice.LatticePoly import LatticePoly
from src.Lattice.LatticePolys import LatticePolys
from . import Example


class Test_LatticePolys:

    basis = Example.basis
    sites = Example.sites
    atoms = Example.atoms
    atoms = LatticeAtoms(basis=basis).make(Example.atoms, sites=sites)
    bonds = Example.bonds
    zro_polys = []
    for center, others in bonds['ZrO'].items():
        zro_polys.append(LatticePoly(atoms.take(others), atoms[center]))
    sio_polys = []
    for center, others in bonds['SiO'].items():
        sio_polys.append(LatticePoly(atoms.take(others), atoms[center]))

    def test__init__zro(self):
        polys = LatticePolys(self.zro_polys, basis=self.basis)
        assert np.array_equal(polys.basis, self.basis)
        for i, poly in enumerate(polys):
            assert poly.center.atom == 'Zr'
            assert np.all(poly.atoms.atoms() == 'O')
            assert len(poly.atoms) == 6

    def test__init__sio(self):
        polys = LatticePolys(self.sio_polys, basis=self.basis)
        assert np.array_equal(polys.basis, self.basis)
        for i, poly in enumerate(polys):
            assert poly.center.atom == 'Si'
            assert np.all(poly.atoms.atoms() == 'O')
            assert len(poly.atoms) == 4

    def test_volume_zro(self):
        polys = LatticePolys(self.zro_polys, basis=self.basis)
        assert np.allclose(polys.volumes(), 12.18189652)

    def test_volume_sio(self):
        polys = LatticePolys(self.sio_polys, basis=self.basis)
        assert np.allclose(polys.volumes(), 2.2704505)

    def test_areas_zro(self):
        polys = LatticePolys(self.zro_polys, basis=self.basis)
        assert np.allclose(polys.areas(), 30.30255177)

    def test_areas_sio(self):
        polys = LatticePolys(self.sio_polys, basis=self.basis)
        assert np.allclose(polys.areas(), 12.46047784)

    def test_make_zro(self):
        polys = LatticePolys(basis=self.basis)
        polys = polys.make(self.atoms['Zr'], self.atoms['O'], 6)
        for i, poly in enumerate(polys):
            assert poly.center == self.zro_polys[i].center
            for atom in poly.atoms:
                assert atom in self.zro_polys[i].atoms

    def test_make_sio(self):
        polys = LatticePolys(basis=self.basis)
        polys = polys.make(self.atoms['Si'], self.atoms['O'], 4)
        for i, poly in enumerate(polys):
            assert poly.center == self.sio_polys[i].center
            for atom in poly.atoms:
                assert atom in self.sio_polys[i].atoms
