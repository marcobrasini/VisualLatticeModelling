import numpy as np
from copy import deepcopy
from src.Lattice.Lattice import Lattice
from src.Lattice.LatticeAtoms import LatticeAtoms
from src.Lattice.LatticeBasis import LatticeBasis
from src.Lattice.LatticeBonds import LatticeBonds
from src.Lattice.LatticePolys import LatticePolys
from . import Example


class Test_Lattice:

    parameter = Example.parameter
    reduced = Example.reduced
    basis = LatticeBasis(reduced, parameter=parameter)

    sites = Example.sites
    atoms = Example.atoms
    atoms = LatticeAtoms(basis=basis).make(atoms, sites=sites)

    bonds = LatticeBonds(basis=basis)
    bonds = bonds.make(atoms['Zr'], atoms['O'], 2.5)
    bonds = bonds.make(atoms['Si'], atoms['O'], 2.0)

    polys = LatticePolys(basis=basis)
    polys = polys.make(atoms['Zr'], atoms['O'], 6)
    polys = polys.make(atoms['Si'], atoms['O'], 4)

    poscar_input = Example.poscar_input
    poscar_output = Example.poscar_output

    matrix = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [1 / 3, 1 / 3, 1 / 3],
    ])
    matrix_super = np.array([
        [-2/3, +4/3, +1/3],
        [+4/3, -2/3, +1/3],
        [-2/3, -2/3, +1/3],
    ])

    def test__init__default(self):
        lattice = Lattice()
        assert lattice.name == ""
        assert np.array_equal(lattice.basis, np.identity(3))
        assert lattice.basis.parameter == 1.0
        assert len(lattice.atoms) == 0
        assert np.array_equal(lattice.atoms.basis, np.identity(3))
        assert len(lattice.bonds) == 0
        assert np.array_equal(lattice.bonds.basis, np.identity(3))
        assert len(lattice.polys) == 0
        assert np.array_equal(lattice.polys.basis, np.identity(3))

    def test__init__basis(self):
        lattice = Lattice("", self.basis)
        assert lattice.name == ""
        assert np.array_equal(lattice.basis, self.basis)
        assert lattice.basis.parameter == self.parameter
        assert len(lattice.atoms) == 0
        assert np.array_equal(lattice.atoms.basis, self.basis)
        assert len(lattice.bonds) == 0
        assert np.array_equal(lattice.bonds.basis, self.basis)
        assert len(lattice.polys) == 0
        assert np.array_equal(lattice.polys.basis, self.basis)

    def test__init__atoms(self):
        lattice = Lattice("", self.basis, self.atoms)
        assert lattice.name == ""
        assert np.array_equal(lattice.basis, self.basis)
        assert lattice.basis.parameter == self.parameter
        assert len(lattice.atoms) == len(self.atoms)
        assert np.array_equal(lattice.atoms.basis, self.basis)
        for i, atom in enumerate(lattice.atoms):
            assert atom == self.atoms[i]
        assert len(lattice.bonds) == 0
        assert np.array_equal(lattice.bonds.basis, self.basis)
        assert len(lattice.polys) == 0
        assert np.array_equal(lattice.polys.basis, self.basis)

    def test__init__bonds(self):
        lattice = Lattice("", self.basis, self.atoms, self.bonds)
        assert lattice.name == ""
        assert np.array_equal(lattice.basis, self.basis)
        assert lattice.basis.parameter == self.parameter
        assert len(lattice.atoms) == len(self.atoms)
        assert np.array_equal(lattice.atoms.basis, self.basis)
        for i, atom in enumerate(lattice.atoms):
            assert atom == self.atoms[i]
        assert len(lattice.bonds) == len(self.bonds)
        assert np.array_equal(lattice.bonds.basis, self.basis)
        for i, bond in enumerate(lattice.bonds):
            assert bond == self.bonds[i]
        assert len(lattice.polys) == 0
        assert np.array_equal(lattice.polys.basis, self.basis)

    def test_transform(self):
        lattice = Lattice("", deepcopy(self.basis), deepcopy(self.atoms))
        lattice = lattice.transform(self.matrix)
        assert len(lattice.atoms) == int(len(self.atoms)/3)

    def test_transform_super(self):
        lattice = Lattice("", deepcopy(self.basis), deepcopy(self.atoms))
        lattice.transform(self.matrix_super)
        assert len(lattice.atoms) == int(len(self.atoms)*4/3)

    def test_load_poscar(self):
        lattice = Lattice.load_poscar(self.poscar_input)
        assert np.array_equal(lattice.basis, self.basis)
        assert lattice.basis.parameter == self.basis.parameter
        assert np.array_equal(lattice.atoms, self.atoms)
        assert np.array_equal(lattice.atoms.basis, self.atoms.basis)

    def test_save_poscar(self):
        Lattice("", self.basis, self.atoms).save_poscar(self.poscar_output)
        saved = Lattice.load_poscar(self.poscar_output)
        assert np.allclose(saved.basis, self.basis)
        assert saved.basis.parameter == self.basis.parameter
        assert saved.atoms.count() == self.atoms.count()
        assert np.allclose(saved.atoms.basis, self.atoms.basis)
        for site in saved.atoms.sites():
            delta = np.isclose(np.abs(self.sites - site), 0.0)
            assert np.sum(np.all(delta, axis=1)) == 1
