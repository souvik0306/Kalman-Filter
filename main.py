import numpy as np
import unittest
import matplotlib.pyplot as plt
from kf import KF

plt.ion()
plt.figure(figsize=(8,5))
kf = KF(initial_x=0.0,initial_v=1.0,accel_variance=0.1)

DT = 0.1
Num_steps = 1000
meas_every_step = 20

real_x = 0.0
real_v = 0.5
meas_variance = 0.1**2

mus = []
covs = []
real_xs = []
real_vs = []

for step in range(Num_steps):
    if step>500:
        real_v *=0.9
    covs.append(kf.cov)
    mus.append(kf.mean)

    real_x = real_x + DT*real_v

    kf.predict(dt=DT)

    if step != 0 and step % meas_every_step == 0:
        kf.update(meas_value = real_x + np.random.randn()*np.sqrt(meas_variance),
        meas_variance=meas_variance)

    real_xs.append(real_x)
    real_vs.append(real_v)

musx_array = [mu[0] for mu in mus]
musx_array = np.array(musx_array)
print("MSE Error for Position: ",'{0:.3f}'.format(((musx_array - real_xs) ** 2).mean(axis=None)*100))
print("RMSE Error for Position: ",'{0:.3f}\n'.format(np.sqrt(((musx_array - real_xs) ** 2).mean(axis=None))*100))

musv_array = [mu[1] for mu in mus]
musv_array = np.array(musv_array)
print("MSE Error for Velocity: ",'{0:.3f}'.format(((musv_array - real_vs) ** 2).mean(axis=None)*100))
print("RMSE Error for Velocity: ",'{0:.3f}'.format(np.sqrt(((musv_array - real_vs) ** 2).mean(axis=None))*100))

plt.subplot(2,1,1)
plt.title('Position')
plt.plot([mu[0] for mu in mus],'g')
plt.plot(real_xs,'b')
plt.plot([mu[0]-2*np.sqrt(cov[0,0]) for mu,cov in zip(mus,covs)],'r--')
plt.plot([mu[0]+2*np.sqrt(cov[0,0]) for mu,cov in zip(mus,covs)],'r--')
plt.legend(['Position','Real_XS','Uncertainity'])

plt.subplot(2,1,2)
plt.title('Velocity')
plt.plot([mu[1] for mu in mus],'g')
plt.plot(real_vs,'b')
plt.plot([mu[1]-2*np.sqrt(cov[1,1]) for mu,cov in zip(mus,covs)],'r--')
plt.plot([mu[1]+2*np.sqrt(cov[1,1]) for mu,cov in zip(mus,covs)],'r--')
plt.legend(['Velocity','Real_VS','Uncertainity'])

plt.show()
plt.ginput(1)