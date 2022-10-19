import numpy as np

class KF:
    def __init__(self, initial_x: float,initial_v: float, accel_variance:float):
        # mean of Gaussian Random Variable
        self._x = np.array([initial_x,initial_v])
        self._acccel_variance = accel_variance
        # covariance of Gaussian Random Variable
        self._P = np.eye(2)
    
    def predict(self, dt:float) -> None:
        F = np.array([[1,dt],[0,1]])
        new_x = F.dot(self._x)
        G = np.array([0.5*dt**2,dt]).reshape((2,1))
        new_P = F.dot(self._P).dot(F.T)+G.dot(G.T)*self._acccel_variance
        self._P = new_P
        self._x = new_x

    def update(self,meas_value:float,meas_variance:float):
        z = np.array([meas_value])
        R = np.array([meas_variance])
        H = np.array([1,0]).reshape((1,2))
        y = z-H.dot(self._x)
        s = H.dot(self._P).dot(H.T)+R
        K = self._P.dot(H.T).dot(np.linalg.inv(s))
        new_x = self._x + K.dot(y)
        new_P = (np.eye(2)-K.dot(H)).dot(self._P)
        self._P = new_P
        self._x = new_x

    @property
    def cov(self) -> np.array:  
        return self._P

    @property
    def mean(self):
        return self._x

    @property
    def pos(self):
        return self._x[0]

    @property
    def vel(self):
        return self._x[1]