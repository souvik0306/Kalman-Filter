import unittest
from kf import KF
import numpy as np

class TestKF(unittest.TestCase):
    def test_can_construct_with_x_and_v(self):
        x = 0.2
        v = 2.3

        kf = KF(initial_x=x,initial_v=v,accel_variance=1.2)
        self.assertAlmostEqual(kf.pos,x)
        self.assertAlmostEqual(kf.vel,v)
    
    def test_can_predict(self):
        x = 0.2
        v = 2.3

        kf = KF(initial_x=x,initial_v=v,accel_variance=1.2)
        kf.predict(dt=0.1)

        self.assertEqual(kf.cov.shape,(2,2))
        self.assertEqual(kf.mean.shape,(2,))

    def test_can_predict(self):
        x = 0.2
        v = 2.3

        kf = KF(initial_x=x,initial_v=v,accel_variance=1.2)
        kf.predict(dt=0.1)

        self.assertEqual(kf.cov.shape,(2,2))
        self.assertEqual(kf.mean.shape,(2,))

    def test_after_calling_predict_increase_state_uncertainty(self):
        x = 0.2
        v = 2.3

        kf = KF(initial_x=x,initial_v=v,accel_variance=1.2)
        for i in range(10):
            det_before = np.linalg.det(kf.cov)
            kf.predict(dt=0.1)
            det_after = np.linalg.det(kf.cov)

            self.assertGreater(det_after,det_before)