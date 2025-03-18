import matplotlib.pyplot as plt

# Data for the celestial bodies
celestial_bodies = ['Earth', 'Mars', 'Jupiter']
first_cosmic_velocity = [7.8, 5.0, 60.2]  # In km/s
second_cosmic_velocity = [11.2, 5.0, 60.0]  # In km/s
third_cosmic_velocity = [42.1, 28.0, 60.0]  # In km/s

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(celestial_bodies, first_cosmic_velocity, label="First Cosmic Velocity", linestyle='-', marker='o')
plt.plot(celestial_bodies, second_cosmic_velocity, label="Second Cosmic Velocity", linestyle='--', marker='o')
plt.plot(celestial_bodies, third_cosmic_velocity, label="Third Cosmic Velocity", linestyle=':', marker='o')

# Adding labels and title
plt.title('Comparison of Cosmic Velocities for Different Celestial Bodies')
plt.xlabel('Celestial Bodies')
plt.ylabel('Velocity (km/s)')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
