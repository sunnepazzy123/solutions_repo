
import numpy as np
import matplotlib.pyplot as plt

# Constants
A = 1         # Amplitude of the wave
wavelength = 2  # Wavelength
frequency = 1  # Frequency (Hz)
omega = 2 * np.pi * frequency  # Angular frequency
k = 2 * np.pi / wavelength  # Wave number
phi = 0  # Initial phase

# Define the polygon (Square) vertices
square_size = 10
sources = np.array([[0, 0], [square_size, 0], [square_size, square_size], [0, square_size]])

# Define the grid for visualization
x = np.linspace(-15, 15, 400)
y = np.linspace(-15, 15, 400)
X, Y = np.meshgrid(x, y)

# Compute the total displacement at each point (X, Y)
displacement = np.zeros(X.shape)

for source in sources:
    # Calculate the distance from each point on the grid to the source
    r = np.sqrt((X - source[0])**2 + (Y - source[1])**2)
    displacement += A * np.cos(k * r - omega * 0 + phi)  # Assume time = 0 for simplicity

# Plot the interference pattern
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, displacement, 50, cmap='jet')
plt.colorbar(label='Displacement')
plt.title('Interference Pattern of Waves from Square Sources')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()