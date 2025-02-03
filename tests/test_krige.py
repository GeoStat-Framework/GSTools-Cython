"""
This is the unittest of the kriging module.
"""

import unittest

import numpy as np

import gstools_cython as gs_cy


class TestKrige(unittest.TestCase):
    def setUp(self):
        # cond_pos = [0.3, 1.9, 1.1]
        # cond_val = [0.47, 0.56, 0.74]
        # x = [0.5, 1.5]
        # model = Gaussian(dim=1, var=0.5, len_scale=2)
        # krig = krige.Simple(model, mean=1, cond_pos=cond_pos, cond_val=cond_val)
        # field, error = krig(x)
        self.krig_mat = np.array(
            [
                [22.779309008408386, 17.71701030060681, -35.714164777816634],
                [17.717010300606795, 22.779309008408426, -35.714164777816656],
                [-35.71416477781662, -35.71416477781667, 64.9934565679449],
            ],
            dtype=np.double,
        )
        self.krig_vecs = np.array(
            [
                [0.49608839014628076, 0.37685660597823356],
                [0.34027802306393057, 0.4845362131524053],
                [0.4658772855496882, 0.4845362131524053],
            ],
            dtype=np.double,
        )
        self.cond = np.array([-0.53, -0.43999999999999995, -0.26], dtype=np.double)

        self.field_ref = np.array([-0.42936306, -0.29739613], dtype=np.double)
        self.error_ref = np.array([0.49987232, 0.49982352], dtype=np.double)

    def test_calc_field_krige_and_variance(self):
        field, error = gs_cy.krige.calc_field_krige_and_variance(
            self.krig_mat, self.krig_vecs, self.cond
        )
        np.testing.assert_allclose(field, self.field_ref)
        np.testing.assert_allclose(error, self.error_ref)

    def test_calc_field_krige(self):
        field = gs_cy.krige.calc_field_krige(self.krig_mat, self.krig_vecs, self.cond)
        np.testing.assert_allclose(field, self.field_ref)


if __name__ == "__main__":
    unittest.main()
