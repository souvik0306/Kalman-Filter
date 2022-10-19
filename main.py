import numpy as np
import unittest
import matplotlib.pyplot as plt
from kf import KF

plt.ion()
plt.figure(figsize=(8,5))
kf = KF(initial_x=0.0,initial_v=1.0,accel_variance=10.0)
DT = 0.1
Num_steps = 1000
mus = []
covs = []

for i in range(Num_steps):
    covs.append(kf.cov)
    mus.append(kf.mean)
    kf.predict(dt=DT)

plt.subplot(2,1,1)
plt.title('Position')
plt.plot([mu[0] for mu in mus],'g')
plt.plot([mu[0]-2*np.sqrt(cov[0,0]) for mu,cov in zip(mus,covs)],'r--')
plt.plot([mu[0]+2*np.sqrt(cov[0,0]) for mu,cov in zip(mus,covs)],'r--')
plt.legend(['Position','Uncertainity'])

plt.subplot(2,1,2)
plt.title('Velocity')
plt.plot([mu[1] for mu in mus],'g')
plt.plot([mu[1]-2*np.sqrt(cov[1,1]) for mu,cov in zip(mus,covs)],'r--')
plt.plot([mu[1]+2*np.sqrt(cov[1,1]) for mu,cov in zip(mus,covs)],'r--')
plt.legend(['Velocity','Uncertainity'])

plt.show()
plt.ginput(1)