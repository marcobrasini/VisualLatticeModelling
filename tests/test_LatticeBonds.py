import numpy as np
from src.pyLattice.LatticeSite import LatticeSite
from src.pyLattice.LatticeSites import LatticeSites
from src.pyLattice.LatticeAtom import LatticeAtom
from src.pyLattice.LatticeAtoms import LatticeAtoms
from src.pyLattice.LatticeBond import LatticeBond
from src.pyLattice.LatticeBonds import LatticeBonds
from . import Example


class Test_LatticeBonds:

    basis = Example.basis
    sites = Example.sites
    atoms = Example.atoms
    atoms = LatticeAtoms(basis=basis).make(atoms, sites=sites)
    bonds = Example.bonds
    zro_bonds = []
    for i in bonds['ZrO'].keys():
        for j in Example.bonds['ZrO'][i]:
            zro_bonds.append(LatticeBond(atoms[i], atoms[j]))
    sio_bonds = []
    for i in bonds['SiO'].keys():
        for j in Example.bonds['SiO'][i]:
            sio_bonds.append(LatticeBond(atoms[i], atoms[j]))
    sio_bonds = sio_bonds

    def test__init__zro(self):
        bonds = LatticeBonds(self.zro_bonds, basis=self.basis)
        assert np.array_equal(bonds.basis, self.basis)
        for i, bond in enumerate(bonds):
            assert bond == self.zro_bonds[i]

    def test__init__sio(self):
        bonds = LatticeBonds(self.sio_bonds, basis=self.basis)
        assert np.array_equal(bonds.basis, self.basis)
        for i, bond in enumerate(bonds):
            assert bond == self.sio_bonds[i]

    def test_atoms1_zro(self):
        bonds = LatticeBonds(self.zro_bonds, basis=self.basis)
        atoms1 = bonds.atoms1()
        assert np.array_equal(atoms1.basis, self.basis)
        assert np.all(atoms1.atoms() == 'Zr')

    def test_atoms2_zro(self):
        bonds = LatticeBonds(self.zro_bonds, basis=self.basis)
        atoms2 = bonds.atoms2()
        assert np.array_equal(atoms2.basis, self.basis)
        assert np.all(atoms2.atoms() == 'O')

    def test_atoms1_sio(self):
        bonds = LatticeBonds(self.sio_bonds, basis=self.basis)
        atoms1 = bonds.atoms1()
        assert np.array_equal(atoms1.basis, self.basis)
        assert np.all(atoms1.atoms() == 'Si')

    def test_atoms2_sio(self):
        bonds = LatticeBonds(self.sio_bonds, basis=self.basis)
        atoms2 = bonds.atoms2()
        assert np.array_equal(atoms2.basis, self.basis)
        assert np.all(atoms2.atoms() == 'O')

    def test_vectors_zro(self):
        bonds = LatticeBonds(self.zro_bonds, basis=self.basis)
        vectors = bonds.vectors()
        assert isinstance(vectors, LatticeSites)
        assert np.array_equal(vectors.basis, self.basis)

    def test_vectors_sio(self):
        bonds = LatticeBonds(self.sio_bonds, basis=self.basis)
        vectors = bonds.vectors()
        assert isinstance(vectors, LatticeSites)
        assert np.array_equal(vectors.basis, self.basis)

    def test_centers_zro(self):
        bonds = LatticeBonds(self.zro_bonds, basis=self.basis)
        centers = bonds.centers()
        assert isinstance(centers, LatticeSites)
        assert np.array_equal(centers.basis, self.basis)

    def test_centers_sio(self):
        bonds = LatticeBonds(self.sio_bonds, basis=self.basis)
        centers = bonds.centers()
        assert isinstance(centers, LatticeSites)
        assert np.array_equal(centers.basis, self.basis)

    def test_versors_zro(self):
        bonds = LatticeBonds(self.zro_bonds, basis=self.basis)
        versors = bonds.versors()
        assert not isinstance(bonds.versors(), LatticeSites)
        assert np.allclose(np.linalg.norm(versors, axis=1), 1.0)

    def test_versors_sio(self):
        bonds = LatticeBonds(self.zro_bonds, basis=self.basis)
        versors = bonds.versors()
        assert not isinstance(bonds.versors(), LatticeSites)
        assert np.allclose(np.linalg.norm(versors, axis=1), 1.0)

    def test_lengths_zro(self):
        bonds = LatticeBonds(self.zro_bonds, basis=self.basis)
        lengths = bonds.lengths()
        assert not isinstance(bonds.lengths(), LatticeSites)
        assert np.all(lengths > 2.045) and np.all(lengths < 2.154)

    def test_lengths_sio(self):
        bonds = LatticeBonds(self.sio_bonds, basis=self.basis)
        lengths = bonds.lengths()
        assert not isinstance(lengths, LatticeSites)
        assert np.all(lengths > 1.642) and np.all(lengths < 1.645)

    def test_make_zro(self):
        bonds = LatticeBonds(basis=self.basis)
        bonds = bonds.make(self.atoms['Zr'], self.atoms['O'], 2.5)
        assert len(bonds) == len(self.zro_bonds)
        for i, bond in enumerate(bonds):
            assert bond in self.zro_bonds

    def test_make_sio(self):
        bonds = LatticeBonds(basis=self.basis)
        bonds = bonds.make(self.atoms['Si'], self.atoms['O'], 2.5)
        assert len(bonds) == len(self.sio_bonds)
        for i, bond in enumerate(bonds):
            assert bond in self.sio_bonds
