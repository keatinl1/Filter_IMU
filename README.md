# IMU Accelerometer Data Processing

## Table of contents
0. [Overview](#overview)
1. [Approach 1: Moving Average Filter](#approach-1-moving-average-filter)
2. [Approach 2: Low Pass Filter](#approach-2-low-pass-filter)
3. [Approach 3: Kalman Filter](#approach-3-kalman-filter)
4. [References](#references)

## Overview
This project involved the processing of accelerometer data obtained from an Arduino IMU. A a moving average filter, low pass filter and a Kalman filter were the approaches used.

Figure 1 shows the noisy raw data that was to be filtered.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/Pre_Filtering.png">
  </kbd>
</p>
<p align="center">
Figure 1: Noisy raw data obtained from the accelerometer.
</p>

$~~~~~~~~~~$

## Approach 1: Moving Average Filter

The intention of the moving average filter was to combine the current acceleration reading with the previous 9 and take the average of them.

The equation is shown here:

$$y[k] = \frac{1}{10}\sum\limits_{i=0}^{9} x[k-i]$$

### Results

The results from the filter are shown in figure 2. It reduced the magnitude of the large peaks from the signal but they were still present, there were also small high frequency readings still present.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/moving_avg.png">
  </kbd>
</p>
<p align="center">
Figure 2: Data after moving average Filter is applied
</p>


$~~~~~~~~~~$

## Approach 2: Low Pass Filter

### Fourier analysis

The process for implementing the LPF was as follows: a discrete Fourier transform of the raw data (using ```numpy.fft()```), a cutoff frequency was chosen, the filter based on this cutoff was then transformed to the Z domain, then inverse Z transformed.

Figure 3 shows the DFT.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/DFT.png">
  </kbd>
</p>
<p align="center">
Figure 3: Discrete Fourier Transform of noisy raw data
</p>

### Designing filter

In figure 3 the red lines show the desired cutoff frequency ( $\omega_{c}$). The LPF was defined with the following transfer function [1]:

$$H(s) = \frac{\omega_{c}}{s + \omega_{c}}$$

It is a single pole also known as a first order low pass filter. A bilinear transform (also known as Tustins method) was performed to get this filter in the Z domain. Then an inverse Z transform to get it in a format which could be implemented in code. See ```\derivation``` to see how to do this.

$$y[k] \approx \left(\frac{2-T\omega_c}{2+T\omega_c}\right)y[k-1] + \left(\frac{T\omega_c}{2+T\omega_c}\right)\left(x[k]+x[k-1]\right)$$

### Results

The resulting plot is shown in figure 4. Most of the high frequency noise is removed or attenuated.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/After_Filtering.png">
  </kbd>
</p>
<p align="center">
Figure 4: Data after low pass filter is applied
</p>

$~~~~~~~~~~$

## Approach 3: Kalman Filter

A Kalman filter was implemented to estimate both acceleration and jerk, allowing for smoother and more robust state estimation.

The system model used was:

$${\left\lbrack \matrix{a_{k+1} \cr \dot{a}_{k+1}}\right\rbrack  = \left\lbrack \matrix{1 & \Delta T \cr 0 & 1}\right\rbrack \begin{bmatrix} a_k \cr \dot{a}_k \end{bmatrix} }$$

The measurement model was:

$$y_k = \begin{bmatrix}1 & 0\end{bmatrix} \begin{bmatrix} a_k \cr \dot{a}_k \end{bmatrix}$$


Where $a_k$ is acceleration, $\dot{a}_k$ is jerk, and $y_k$ is the measured acceleration.

### Implementation

A standard linear Kalman filter was implemented with the following steps:

**Prediction Step:**\
Where $Q$ is process noise covariance,

\
$x_{k}^- = A x_{k-1}$

\
$P_{k}^- = A P_{k-1} A^T + Q$


**Update Step:**\
Where $R$ is measurement noise covariance,

\
$K_k = \frac{P_k^- C^T}{C P_k^- C^T + R}$

\
$x_k = x_k^- + K_k (y_k - C x_k^-)$

\
$P_k = (I - K_k C) P_k^-$


### Results

The Kalman filter effectively smoothed the acceleration readings and provided an estimate of jerk. Figure 5 shows the results, demonstrating noise attenuation.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/kalman.png">
  </kbd>
</p>
<p align="center">
Figure 5: Data after Kalman filter is applied
</p>

The evolution of the trace of the error covariance matrix was also plotted it is shown in figure 6. The trace reduced from the initial guess until stabilising at the value of $P_\infty$ which is the solution of the Ricatti equation

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/kalman_trace.png">
  </kbd>
</p>
<p align="center">
Figure 6: Trace of error covariance matrix
</p>


$~~~~~~~~~~$

## References

[1] - Kamenetsky, M. (2003). Filtered Audio Demo [Lecture notes]. Stanford University. Retrieved from https://web.stanford.edu/~boyd/ee102/conv_demo.pdf




