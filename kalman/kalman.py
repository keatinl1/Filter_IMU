import numpy as np
import matplotlib.pyplot as plt
import csv

# Load data from CSV
x_data, y_data, z_data = [], [], []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        x_data.append(float(row[0]))
        y_data.append(float(row[1]))
        z_data.append(float(row[2]))

# Define the Kalman Filter class
class Kalman:
    def __init__(self):
        self.dt = 0.018

        self.A = np.array([[1, self.dt], [0, 1]])
        self.C = np.array([[1, 0]])
        
        self.Q = np.identity(2)*0.002
        self.R = np.identity(1)*0.1
        
        self.P = np.eye(2)  # Initial error covariance
        self.x = np.array([[0], [0]])  # Initial state: [acceleration, jerk]

    def predict(self):
        """ Predict the next state and error covariance """
        self.x = self.A @ self.x  # x_k+1 = A * x_k
        self.P = self.A @ self.P @ self.A.T + self.Q  # P_k+1(-) = A * P_k * A^T + Q
    
    def update(self, measurement):
        """ Update the state estimate with a new measurement """
        K = (self.P @ self.C.T) / (self.C @ self.P @ self.C.T + self.R)
        self.x = self.x + K * (measurement - self.C@self.x)
        self.P = (np.eye(2) - K @ self.C) @ self.P

    def get_state(self):
        """ Return the current estimated acceleration"""
        return self.x[0, 0], self.P

# Initialize Kalman filters for each axis
kalman_x = Kalman()
kalman_y = Kalman()
kalman_z = Kalman()

# Store filtered data
x_out, y_out, z_out = [], [], []

p_out = []

# Apply Kalman filter to the data
for k in range(len(x_data)):
    kalman_x.predict()
    kalman_y.predict()
    kalman_z.predict()
    
    kalman_x.update(x_data[k])
    kalman_y.update(y_data[k])
    kalman_z.update(z_data[k])
    
    a_x, Px = kalman_x.get_state()
    a_y, _ = kalman_y.get_state()
    a_z, _ = kalman_z.get_state()

    x_out.append(a_x)
    y_out.append(a_y)
    z_out.append(a_z)

    print_P = sum(sum(Px))
    p_out.append(print_P)


# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_out, label='Filtered X')
plt.plot(y_out, label='Filtered Y')
plt.plot(z_out, label='Filtered Z')

# plt.plot(x_data, label='Original X')
# plt.plot(y_data, label='Original Y')
# plt.plot(z_data, label='Original Z')

plt.figure(figsize=(8, 6))
plt.plot(p_out, label='P out')

plt.legend()
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Filtered Data')
plt.show()
