import matplotlib.pyplot as plt
import numpy as np

# Load data from file
file_path = 'data.csv'  # Replace with your file path
with open(file_path, 'r') as file:
    lines = file.readlines()

# Initialize empty lists to store logged data
x_data, y_data, z_data = [], [], []

# Parse the data
for line in lines:
    values = line.strip().split(',')
    if len(values) == 3:
        x, y, z = map(float, values)
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)

# Calculate the time interval assuming uniform time between samples
time_interval = 0.018  # Replace with the actual time interval between samples

# Compute DFT for x, y, z data
x_fft = np.fft.fft(x_data)
y_fft = np.fft.fft(y_data)
z_fft = np.fft.fft(z_data)

# Calculate frequencies for the DFT plot
sampling_rate = 1 / time_interval
freq = np.fft.fftfreq(len(x_data), d=1/sampling_rate)

# Plot individual frequency domain data (DFT) for x, y, z with different colors
plt.figure(figsize=(8, 18))

plt.subplot(3, 1, 1)
plt.plot(freq, np.abs(x_fft), color='blue', linewidth=1.0)
plt.title('Frequency Domain Data (DFT) - X, Y, Z')
# plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(freq, np.abs(y_fft), color='orange', linewidth=1.0)
# plt.title('Frequency Domain Data (DFT) - Y')
# plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(freq, np.abs(z_fft), color='green', linewidth=1.0)
# plt.title('Frequency Domain Data (DFT) - Z')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

# plt.tight_layout()
plt.show()
