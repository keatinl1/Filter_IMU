# IMU Accelerometer Data Processing

This project involves processing IMU accelerometer data obtained from an Arduino. The process includes conducting a Discrete Fourier Transform (DFT) on the raw data, choosing a cutoff frequency at 3.7 rad/s, designing a low-pass filter based on this cutoff, and implementing the filter in the discrete domain for signal processing.
Overview. My intention is to implement a simple low pass filter (LPF) and a more advanced Kalman Filter.

## Low Pass Filter

### Initial readings

Shown in figure 1 is the noisy raw data.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/Pre_Filtering.png">
  </kbd>
</p>
<p align="center">
Figure 1
</p>

### Fourier analysis

After recording the data the discrete fourier transform was found using the ```numpy.fft()``` function. It is shown here in figure 2.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/DFT.png">
  </kbd>
</p>
<p align="center">
Figure 2
</p>

### Designing filterAfter_Filtering.png

As shown in figure 2 the red lines show the desired cutoff frequency( $\omega_{c}$). We use the equation:

$H(s) = \frac{\omega_{c}}{s + \omega_{c}}$

Then to get this in discrete time the output is

$y[k] = \frac{\omega_{c}T_s}{1 + \omega_{c}T_s}u[k] + \frac{1}{1 + \omega_{c}T_s}y[k-1]$

### Results and conclusion

The resulting plot is shown in figure 3.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/After_Filtering.png">
  </kbd>
</p>
<p align="center">
Figure 3
</p>

Much of the high frequency noise is removed or attenuated.

## Kalman Filter

### To do...
