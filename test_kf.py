import unittest
from kf import KF

class TestKF(unittest.TestCase):
    def test_can_construct_with_x_and_v(self):
        x = 0.2
        v = 2.3

        kf = KF(initial_x=x,initial_v=v)
        self.assertAlmostEqual(kf.x[0],x)
        self.assertAlmostEqual(kf.x[1],v)