"""
This is a unittest of the variogram module.
"""

import unittest

import numpy as np

import gstools_cython as gs_cy


class TestVariogram(unittest.TestCase):
    def test_directional(self):
        x_c = np.linspace(0.0, 100.0, 30)
        y_c = np.linspace(0.0, 100.0, 30)
        x, y = np.meshgrid(x_c, y_c)
        x = np.reshape(x, len(x_c) * len(y_c))
        y = np.reshape(y, len(x_c) * len(y_c))
        pos = np.array((x, y), dtype=np.double)
        dirs = np.array(((1, 0), (0, 1)), dtype=np.double)

        rng = np.random.RandomState(1479373475)
        field = np.asarray([rng.rand(len(x))], dtype=np.double)
        bins = np.arange(0, 100, 10, dtype=np.double)

        var = 1.0 / 12.0

        gamma, counts = gs_cy.variogram.directional(field, bins, pos, dirs)
        print(counts)
        self.assertAlmostEqual(gamma[0, 0], var, places=2)
        self.assertAlmostEqual(gamma[0, len(gamma[0]) // 2], var, places=2)
        self.assertAlmostEqual(gamma[0, -1], var, places=2)
        self.assertAlmostEqual(gamma[1, 0], var, places=2)
        self.assertAlmostEqual(gamma[1, len(gamma[0]) // 2], var, places=2)
        self.assertAlmostEqual(gamma[1, -1], var, places=2)

    def test_unstructured(self):
        x = np.arange(1, 11, 1, dtype=np.double)
        z = np.array(
            (41.2, 40.2, 39.7, 39.2, 40.1, 38.3, 39.1, 40.0, 41.1, 40.3),
            dtype=np.double,
        )
        bins = np.arange(1, 11, 1, dtype=np.double)
        x = np.atleast_2d(x)
        z = np.atleast_2d(z)

        gamma, counts = gs_cy.variogram.unstructured(z, bins, x)
        self.assertAlmostEqual(gamma[0], 0.4917, places=4)
        self.assertEqual(counts[0], 9)

        x_c = np.linspace(0.0, 100.0, 30)
        y_c = np.linspace(0.0, 100.0, 30)
        x, y = np.meshgrid(x_c, y_c)
        x = np.reshape(x, len(x_c) * len(y_c))
        y = np.reshape(y, len(x_c) * len(y_c))
        pos = np.array((x, y), dtype=np.double)

        rng = np.random.RandomState(1479373475)
        field = np.asarray([rng.rand(len(x))], dtype=np.double)
        bins = np.arange(0, 100, 10, dtype=np.double)

        var = 1.0 / 12.0

        gamma, counts = gs_cy.variogram.unstructured(field, bins, pos)
        self.assertAlmostEqual(gamma[0], var, places=2)
        self.assertAlmostEqual(gamma[len(gamma) // 2], var, places=2)
        self.assertAlmostEqual(gamma[-1], var, places=2)

        gamma, counts = gs_cy.variogram.unstructured(
            field, bins, pos, estimator_type="c"
        )
        self.assertAlmostEqual(gamma[0], var, places=2)
        self.assertAlmostEqual(gamma[len(gamma) // 2], var, places=2)
        self.assertAlmostEqual(gamma[-1], var, places=2)

    def test_structured(self):
        z = np.array(
            (41.2, 40.2, 39.7, 39.2, 40.1, 38.3, 39.1, 40.0, 41.1, 40.3),
            dtype=np.double,
        )
        # need 2d arrays
        z = z.reshape((z.shape[0], -1))

        gamma = gs_cy.variogram.structured(z)
        self.assertAlmostEqual(gamma[1], 0.4917, places=4)

        gamma = gs_cy.variogram.structured(z, estimator_type="c")
        self.assertAlmostEqual(gamma[1], 1.546 / 2.0, places=3)

        rng = np.random.RandomState(1479373475)
        field = np.asarray(rng.rand(80, 60), dtype=np.double)

        gamma = gs_cy.variogram.structured(field)
        var = 1.0 / 12.0
        self.assertAlmostEqual(gamma[0], 0.0, places=2)
        self.assertAlmostEqual(gamma[len(gamma) // 2], var, places=2)
        self.assertAlmostEqual(gamma[-1], var, places=2)

        gamma = gs_cy.variogram.structured(field, estimator_type="c")
        var = 1.0 / 12.0
        self.assertAlmostEqual(gamma[0], 0.0, places=2)
        self.assertAlmostEqual(gamma[len(gamma) // 2], var, places=2)
        self.assertAlmostEqual(gamma[-1], var, places=1)

    def test_ma_structured(self):
        z = np.array(
            (41.2, 40.2, 39.7, 39.2, 40.1, 38.3, 39.1, 40.0, 41.1, 40.3),
            dtype=np.double,
        )
        mask = np.array((1, 0, 0, 0, 0, 0, 0, 0, 0, 0), dtype=bool)
        # need 2d arrays
        z = z.reshape((z.shape[0], -1))
        mask = mask.reshape((mask.shape[0], -1))

        gamma = gs_cy.variogram.ma_structured(z, mask)
        self.assertAlmostEqual(gamma[0], 0.0000, places=4)
        self.assertAlmostEqual(gamma[1], 0.4906, places=4)
        self.assertAlmostEqual(gamma[2], 0.7107, places=4)

        gamma = gs_cy.variogram.ma_structured(z, mask, estimator_type="c")
        self.assertAlmostEqual(gamma[0], 0.0000, places=4)
        self.assertAlmostEqual(gamma[1], 0.7399, places=4)
        self.assertAlmostEqual(gamma[2], 0.8660, places=4)

        rng = np.random.RandomState(1479373475)
        field = np.asarray(rng.rand(80, 60), dtype=np.double)
        mask = np.zeros_like(field, dtype=bool)
        mask[0, 0] = 1

        gamma = gs_cy.variogram.ma_structured(field, mask)
        var = 1.0 / 12.0
        self.assertAlmostEqual(gamma[0], 0.0, places=2)
        self.assertAlmostEqual(gamma[len(gamma) // 2], var, places=2)
        self.assertAlmostEqual(gamma[-1], var, places=2)

        gamma = gs_cy.variogram.ma_structured(field, mask, estimator_type="c")
        var = 1.0 / 12.0
        self.assertAlmostEqual(gamma[0], 0.0, places=2)
        self.assertAlmostEqual(gamma[len(gamma) // 2], var, places=2)
        self.assertAlmostEqual(gamma[-1], var, places=2)


if __name__ == "__main__":
    unittest.main()
