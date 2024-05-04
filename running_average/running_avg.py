import matplotlib.pyplot as plt
import csv

# Function to calculate running average
def running_average(data, window_size):
    return [sum(data[i:i+window_size]) / window_size for i in range(len(data) - window_size + 1)]

# Initialize empty lists to store data
x_data, y_data, z_data = [], [], []

# Read data from the CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        x_data.append(float(row[0]))
        y_data.append(float(row[1]))
        z_data.append(float(row[2]))

# Define the window size for the running average
window_size = 10

# Calculate running averages for X, Y, and Z data
x_out = running_average(x_data, window_size)
y_out = running_average(y_data, window_size)
z_out = running_average(z_data, window_size)

# Plotting
plt.figure(figsize=(8, 6))
# plt.plot(x_data, label='Original X')
plt.plot(range(window_size - 1, len(x_data)), x_out, label='Filtered X')
# plt.plot(y_data, label='Original Y')
plt.plot(range(window_size - 1, len(y_data)), y_out, label='Filtered Y')
# plt.plot(z_data, label='Original Z')
plt.plot(range(window_size - 1, len(z_data)), z_out, label='Filtered Z')
plt.legend()
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Filtered Data')
plt.show()
