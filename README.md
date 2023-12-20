# IMU Accelerometer Data Processing

## Table of contents
0. [Overview](#overview)
1. [Approach 1: Low Pass Filter](#approach-1-low-pass-filter)
2. [Approach 2: Complimentary Filter](#approach-2-complimentary-filter)
3. [Approach 3: Kalman Filter](#approach-3-kalman-filter)
4. [References](#references)

## Overview
This project involves processing IMU accelerometer data obtained from an Arduino. The process includes conducting a Discrete Fourier Transform (DFT) on the raw data, choosing a cutoff frequency at 3.7 rad/s, designing a low-pass filter based on this cutoff, and implementing the filter in the discrete domain for signal processing.
Overview. My intention is to implement a simple low pass filter (LPF), a complimentary filter and a more advanced Kalman Filter.

Shown below in figure 1 is the noisy raw data which we will attempt to filter.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/Pre_Filtering.png">
  </kbd>
</p>
<p align="center">
Figure 1: Noisy raw data obtained from the accelerometer.
</p>

$~~~~~~~~~~$

## Approach 1: Low Pass Filter

### Fourier analysis

After recording the data the discrete fourier transform was found using the ```numpy.fft()``` function. It is shown here in figure 2.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/DFT.png">
  </kbd>
</p>
<p align="center">
Figure 2: Discrete Fourier Transform of noisy raw data
</p>

### Designing filter

In figure 2 the red lines show the desired cutoff frequency ( $\omega_{c}$). We define the LPF with the following transfer function [1]:

$$H(s) = \frac{\omega_{c}}{s + \omega_{c}}$$

You apply a bilinear transform (also known as Tustins method) to get this filter in the Z domain. Then you inverse Z transform to get it in a format we can implement in code. See ```\derivation``` if you wan to see how to do this.

$$y_k \approx \left(\frac{2-T\omega_c}{2+T\omega_c}\right)y_{k-1} + \left(\frac{T\omega_c}{2+T\omega_c}\right)\left(x_k+x_{k-1}\right),$$

### Results

The resulting plot is shown in figure 3. Most of the high frequency noise is removed or attenuated.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/After_Filtering.png">
  </kbd>
</p>
<p align="center">
Figure 3: Data after low pass filter is applied
</p>

$~~~~~~~~~~$

## Approach 2: Complimentary Filter

The same readings as the LPF were used. The intention with the complimentary filter was to combine the current acceleration readings with a moving average of the last 10 outputs.

The equation is shown here:

$$y[k] = (\alpha) \cdot x[k] + (1 - \alpha)\cdot\frac{1}{10}\sum\limits_{i=1}^{10} y[k-i]$$

### Results

The results from the complimentary filter are shown in figure 4. It removes the large peaks from the signal but there is still high frequency readings lingering in the readings.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/complimentary_moving_avg.png">
  </kbd>
</p>
<p align="center">
Figure 4: Data after complimentary filter is applied
</p>

$~~~~~~~~~~$

## Approach 3: Kalman Filter

### To do...

## References

[1] - Kamenetsky, M. (2003). Filtered Audio Demo [Lecture notes]. Stanford University. Retrieved from https://web.stanford.edu/~boyd/ee102/conv_demo.pdf
