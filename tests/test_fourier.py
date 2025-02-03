"""
This is the unittest of the Fourier class.
"""

import unittest
from pathlib import Path

import numpy as np

import gstools_cython as gs_cy


class TestFourier(unittest.TestCase):
    def setUp(self):
        here = Path(__file__).parent
        self.dir = here / "data"
        self.file = "fourier_gen_dim_{dim}_{name}.txt"

    def test_1d(self):
        factor = np.loadtxt(self.dir / self.file.format(dim=1, name="factor"))
        modes = np.loadtxt(self.dir / self.file.format(dim=1, name="modes"), ndmin=2)
        z_1 = np.loadtxt(self.dir / self.file.format(dim=1, name="z_1"))
        z_2 = np.loadtxt(self.dir / self.file.format(dim=1, name="z_2"))
        pos = np.loadtxt(self.dir / self.file.format(dim=1, name="pos"), ndmin=2)
        summed = np.loadtxt(self.dir / self.file.format(dim=1, name="summed"))
        summed_modes = gs_cy.field.summate_fourier(factor, modes, z_1, z_2, pos)
        np.testing.assert_array_almost_equal(summed_modes, summed)

    def test_2d(self):
        factor = np.loadtxt(self.dir / self.file.format(dim=2, name="factor"))
        modes = np.loadtxt(self.dir / self.file.format(dim=2, name="modes"), ndmin=2)
        z_1 = np.loadtxt(self.dir / self.file.format(dim=2, name="z_1"))
        z_2 = np.loadtxt(self.dir / self.file.format(dim=2, name="z_2"))
        pos = np.loadtxt(self.dir / self.file.format(dim=2, name="pos"), ndmin=2)
        summed = np.loadtxt(self.dir / self.file.format(dim=2, name="summed"))
        summed_modes = gs_cy.field.summate_fourier(factor, modes, z_1, z_2, pos)
        np.testing.assert_array_almost_equal(summed_modes, summed)


if __name__ == "__main__":
    unittest.main()
