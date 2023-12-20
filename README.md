# IMU Accelerometer Data Processing

This project involves processing IMU accelerometer data obtained from an Arduino. The process includes conducting a Discrete Fourier Transform (DFT) on the raw data, choosing a cutoff frequency at 3.7 rad/s, designing a low-pass filter based on this cutoff, and implementing the filter in the discrete domain for signal processing.
Overview. My intention is to implement a simple low pass filter (LPF), a complimentary filter and a more advanced Kalman Filter.

## Low Pass Filter

### Initial readings

Shown in figure 1 is the noisy raw data.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/Pre_Filtering.png">
  </kbd>
</p>
<p align="center">
Figure 1: Noisy raw data obtained from the accelerometer.
</p>

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

### Designing filterAfter_Filtering.png

As shown in figure 2 the red lines show the desired cutoff frequency ( $\omega_{c}$). We use the equation:

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
Figure 3: Data after low pass filter is applied
</p>

Much of the high frequency noise is removed or attenuated.

## Complimentary Filter

The same readings as the LPF were used. The intention with the complimentary filter was to combine the current acceleration readings with a moving average of the last 10 outputs.

The equation is shown in equation XX:

$y[k] = (\alpha) x[k] + (1 - \alpha)\frac{\Sigma (y[k-1],...,y[k-11])}{10}$

# Results

The results from the compliemntary filter are shown in figure 4. It removes the large peaks from the signal but there is still high frequency readings lingering in the readings.

<p align="center">
  <kbd>
    <img src="https://raw.githubusercontent.com/keatinl1/Filter_IMU/main/figs/complimentary_moving_avg.png">
  </kbd>
</p>
<p align="center">
Figure 4: Data after complimentary filter is applied
</p>

## Kalman Filter

### To do...
