## Kalman Filter
The Kalman Filter (KF) is a set of mathematical equations that when operating together implement a predictor-corrector type of estimator that is optimal in the sense that it minimizes the estimated error covariance when some presumed conditions are met.

```
Kalman Filtering can be understood as a way of making sense of a noisy world.
```
### The algorithm works in a two-step process. - 

1. In the prediction step, the Kalman filter produces estimates of the current state variables, along with their uncertainties. 

2. Once the outcome of the next measurement (necessarily corrupted with some amount of error, including random noise) is observed, these estimates are updated using a weighted average, with more weight being given to estimates with higher certainty.

## Results - 
• Developed Kalman Filter-based state estimation model for precise approximation & visualization of a robot’s state. 

• Attained an extremely low Mean Square Error of 2.8% & 1.1% for the robot’s position & velocity on evaluation.