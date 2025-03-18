import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_earth = 5.972e24  # Mass of Earth (kg)
R_earth = 6371e3  # Radius of Earth (m)

# Initial conditions (position in meters, velocity in m/s)
r0 = np.array([R_earth + 500e3, 0])  # Payload starts 500 km above Earth's surface
v0 = np.array([0, 7.8e3])  # Initial velocity (approx orbital velocity in m/s)

# Time parameters
dt = 10  # Time step (seconds)
t_max = 10000  # Maximum simulation time (seconds)

# Define the system of differential equations
def gravity(t, state):
    r = state[:2]
    v = state[2:]
    r_magnitude = np.linalg.norm(r)
    a = -G * M_earth * r / r_magnitude**3
    return np.concatenate([v, a])

# Runge-Kutta method to solve the system of equations
def runge_kutta(f, t0, tf, dt, state0):
    t_values = np.arange(t0, tf, dt)
    states = np.zeros((len(t_values), len(state0)))
    states[0] = state0
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        state = states[i-1]
        k1 = f(t, state)
        k2 = f(t + dt / 2, state + dt / 2 * k1)
        k3 = f(t + dt / 2, state + dt / 2 * k2)
        k4 = f(t + dt, state + dt * k3)
        states[i] = state + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)
    return t_values, states

# Solve the system
t_values, states = runge_kutta(gravity, 0, t_max, dt, np.concatenate([r0, v0]))

# Extract position data for plotting
x = states[:, 0]
y = states[:, 1]

# Plot the trajectory
plt.figure(figsize=(8, 8))
plt.plot(x / 1e3, y / 1e3, label="Payload Trajectory")
plt.scatter(0, 0, color="red", label="Earth", s=100)
plt.title("Payload Trajectory Near Earth")
plt.xlabel("X (km)")
plt.ylabel("Y (km)")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()