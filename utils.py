import numpy as np
from filterpy.kalman import KalmanFilter

class Kalman2D:
    def __init__(self):
        self.kf = KalmanFilter(dim_x=4, dim_z=2)

        self.kf.x = np.array([0, 0, 0, 0])

        self.kf.F = np.array([
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        self.kf.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ])

        self.kf.P *= 1000
        self.kf.R = np.eye(2) * 5
        self.kf.Q = np.eye(4) * 0.01

    def update(self, x, y):
        self.kf.predict()
        self.kf.update([x, y])
        return int(self.kf.x[0]), int(self.kf.x[1])