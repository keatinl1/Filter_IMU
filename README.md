# IMU Accelerometer Data Processing

This project involves processing IMU accelerometer data obtained from an Arduino. The process includes conducting a Discrete Fourier Transform (DFT) on the raw data, choosing a cutoff frequency at 3.7 rad/s, designing a low-pass filter based on this cutoff, and implementing the filter in the discrete domain for signal processing.
Overview. My intention is to implement a simple low pass filter (LPF) and a more advanced Kalman Filter.

## Low Pass Filter

### Initial readings

Shown in figure 1 is the noise raw data.

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

### Designing filter

As shown in figure 2 the red lines show the desired cutoff frequency( $\omega_{c}$). We use the equation:




### Results and conclusion


## Kalman Filter

### To do...
