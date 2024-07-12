"""
This is a unittest of the variogram module.
"""

import unittest

import numpy as np

import gstools_cython as gs_cy


class TestVariogram(unittest.TestCase):
    def test_directional(self): ...

    def test_unstructured(self): ...

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
        mask = np.array((1, 0, 0, 0, 0, 0, 0, 0, 0, 0), dtype=np.int32)
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
        mask = np.zeros_like(field, dtype=np.int32)
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
