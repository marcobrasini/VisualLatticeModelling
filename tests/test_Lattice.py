import numpy as np

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

    def test_load_poscar(self):
        lattice = Lattice().load_poscar(self.poscar_input)
        assert np.array_equal(lattice.basis, self.basis)
        assert lattice.basis.parameter == self.basis.parameter
        assert np.array_equal(lattice.atoms, self.atoms)
        assert np.array_equal(lattice.atoms.basis, self.atoms.basis)

    def test_load_poscar(self):
        lattice = Lattice("", self.basis, self.atoms)
        lattice = lattice.save_poscar(self.poscar_output)
