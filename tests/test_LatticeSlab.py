import pytest
import numpy as np
from src.Lattice.Lattice import Lattice
from src.Lattice.LatticeBasis import LatticeBasis
from src.Lattice.LatticeAtoms import LatticeAtoms
from src.Lattice.LatticeSuper import LatticeSuper
from src.Lattice.LatticePlane import LatticePlane
from src.Lattice.LatticeSlab import LatticeSlab
from . import Example


class Test_LatticeSlab:

   axis = 1
   index = [1,2,0]
   ncell = [2,1,1]
   plane = LatticePlane(index)

   # Properties to test:
   supercell = LatticeSuper(ncell)
   # - name
   name = "test"
   slabname = "test_(1,2,0)"
   # - basis
   basis = Example.basis
   superbasis = supercell.basis(basis)
   for i in range(3):
      if i != axis:
         if index[i] != 0:
            superbasis[i] -= superbasis[axis]
   superbasis = np.roll(superbasis, 2 - axis, axis=0)
   # atoms
   atoms = Example.atoms
   superatoms = supercell.atoms(atoms)
   # sites
   sites = Example.sites
   supersites = supercell.sites(sites)

   def test__init__(self):
      slabcell = LatticeSlab(self.index, self.axis)
      assert slabcell.axis == self.axis
      assert slabcell.plane == self.plane
      assert np.all(slabcell.index == self.ncell)

   def test__init__axis(self):
      with pytest.raises(IndexError):
         LatticeSlab(self.index, 2)

   def test_name(self):
      slabcell = LatticeSlab(self.index, self.axis)
      assert slabcell.name() == "(1,2,0)"

   def test_make_name(self):
      slabcell = LatticeSlab(self.index, self.axis)
      slabname = slabcell.make_name(self.name)
      assert slabname == self.slabname

   def test_basis(self):
      slabcell = LatticeSlab(self.index, self.axis)
      slabbasis = slabcell.basis(self.basis)
      assert np.array_equal(slabbasis, self.superbasis)

   def test_make_basis(self):
      basis = LatticeBasis(self.basis, 2)
      slabcell = LatticeSlab(self.index, self.axis)
      slabbasis = slabcell.make_basis(basis)
      assert isinstance(slabbasis, LatticeBasis)
      assert np.array_equal(slabbasis, 2 * self.superbasis)
      assert slabbasis.parameter == basis.parameter

   def test_sites(self):
      slabcell = LatticeSlab(self.index, self.axis)
      slabsites = slabcell.sites(self.sites)
      assert slabsites.shape == self.supersites.shape
      assert np.all(slabcell.plane(slabsites) >= 0)
      assert np.all(slabcell.plane(slabsites) < +1)

   def test_atoms(self):
      slabcell = LatticeSlab(self.index, self.axis)
      slabatoms = slabcell.atoms(self.atoms)
      assert np.array_equal(slabatoms, self.superatoms)

   def test_make_atoms(self):
      atoms = LatticeAtoms(basis=self.basis).make(self.atoms, sites=self.sites)
      slabcell = LatticeSlab(self.index, self.axis)
      slabatoms = slabcell.make_atoms(atoms, self.superbasis)
      assert isinstance(slabatoms, LatticeAtoms)
      assert np.array_equal(slabatoms.basis, self.superbasis)
      assert np.array_equal(slabatoms.atoms(), self.superatoms)
      assert slabatoms.sites().shape == self.supersites.shape
