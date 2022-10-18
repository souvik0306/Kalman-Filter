import numpy as np

class KF:
    def __init__(self, initial_x,initial_v):
        # mean of Gaussian Random Variable
        self.x = np.array([initial_x,initial_v])

        # covariance of Gaussian Random Variable
        self.P = np.eye(2)