## Kalman Filter
The Kalman Filter (KF) is a set of mathematical equations that when operating together implement a predictor-corrector type of estimator that is optimal in the sense that it minimizes the estimated error covariance when some presumed conditions are met.

```
Kalman Filtering can be understood as a way of making sense of a noisy world.
```
### The algorithm works in a two-step process. - 

1. In the prediction step, the Kalman filter produces estimates of the current state variables, along with their uncertainties. 

2. Once the outcome of the next measurement (necessarily corrupted with some amount of error, including random noise) is observed, these estimates are updated using a weighted average, with more weight being given to estimates with higher certainty.

## Simulation Results - 
 
 Ego Robot's Initial State      | Ego State with Noise |
| :-----------: | :-----------: |
|   <image src="https://github.com/souvik0306/Kalman-Filter/blob/main/Media/Figure_2.png" width="450" height="350"> | <image src="https://github.com/souvik0306/Kalman-Filter/blob/main/Media/Figure_3_noise.png" width="450" height="350"> |
 
 Ground Truth vs Estimated     | Ego State with Disturbance |
| :-----------: | :-----------: |
|   <image src="https://github.com/souvik0306/Kalman-Filter/blob/main/Media/Figure_5_analysis.png" width="450" height="350"> | <image src="https://github.com/souvik0306/Kalman-Filter/blob/main/Media/Figure_6_analysis.png" width="450" height="350"> |

## Results - 
• Developed Kalman Filter-based state estimation model for precise approximation & visualization of a robot’s state. 

• Attained an extremely low Mean Square Error of 2.8% & 1.1% for the robot’s position & velocity on evaluation.
