import matplotlib.pyplot as plt
import csv

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

# Define complementary filter function
def complementary_filter(current_value, last_values):
    alpha = 0.4  # Adjustment factor, you can tweak this as needed
    return alpha * current_value + (1 - alpha) * sum(last_values) / len(last_values)
x_out, y_out, z_out = [], [], []
window_size = 10
x_window, y_window, z_window = [], [], []

for i in range(len(x_data)):
    if i >= window_size:
        x_filtered = complementary_filter(x_data[i], x_window)
        y_filtered = complementary_filter(y_data[i], y_window)
        z_filtered = complementary_filter(z_data[i], z_window)
        x_out.append(x_filtered)
        y_out.append(y_filtered)
        z_out.append(z_filtered)
        x_window.pop(0)
        y_window.pop(0)
        z_window.pop(0)

    else:
        x_out.append(x_data[i])
        y_out.append(y_data[i])
        z_out.append(z_data[i])

    x_window.append(x_out[i])
    y_window.append(y_out[i])
    z_window.append(z_out[i])

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_data, label='Original X')
plt.plot(x_out, label='Filtered X')
plt.plot(y_data, label='Original Y')
plt.plot(y_out, label='Filtered Y')
plt.plot(z_data, label='Original Z')
plt.plot(z_out, label='Filtered Z')
plt.legend()
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Filtered Data')
plt.show()
