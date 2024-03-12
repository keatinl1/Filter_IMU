# IMU Accelerometer Data Processing

## Table of contents
0. [Overview](#overview)
1. [Approach 1: Moving Average Filter](#approach-1-moving-average-filter)
2. [Approach 2: Low Pass Filter](#approach-2-low-pass-filter)
3. [Approach 3: Chebyshev Filter](#approach-3-chebyshev-filter)
4. [Approach 4: Kalman Filter](#approach-4-kalman-filter)
5. [References](#references)

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
Figure 2: Data after complimentary filter is applied
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

## Approach 3: Chebyshev Filter

Chebyshev filters are also designed using frequency analysis but they have faster rolloff than a standard low pass filter (at the expense of ripples in the passband (in the type 1 version)).

When the ripple percentage is set to zero, this is known as a Butterworth filter, but in this exampl a ripple percentage of 0.5% will be set as the ripple is negligable and the rolloff is even quicker than the Butterworth version.

Figure 5 shows what is meant by ripple, the solid line shows the 0% ripple Butterworth filter:

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/ripple.png">
  </kbd>
</p>
<p align="center">
Figure 5: Comparison of ripple percentages
</p>


The transfer function is shown below

$$H(s) = \frac{1}{1 + \epsilon^2(T_{n}(\frac{s}{\omega_{c}}))^2}$$

Where $T_n(x)$ is a Chebyshev polynomial as is calculated as so,

$$
\begin{aligned}
&T_0(x)= 1 \\
&T_1(x)= x \\
&T_{n+1}(x)= 2x \cdot T_n(x) - T_{n-1}(x)
\end{aligned}
$$

For a fair comparison to the first order filter above, a first order Chebyshev polynomial will be chosen so $T_{n}(\frac{s}{\omega_{c}}) = \frac{s}{\omega_{c}}$.
$~~~~~~~~~~$

## Approach 4: Kalman Filter

To do...

## References

[1] - Kamenetsky, M. (2003). Filtered Audio Demo [Lecture notes]. Stanford University. Retrieved from https://web.stanford.edu/~boyd/ee102/conv_demo.pdf
