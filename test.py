import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import m_p, e, epsilon_0, mu_0

# Constants
q = e  # Charge of particle (Coulombs)
m = m_p  # Mass of particle (kg)
B = np.array([0, 0, 1])  # Magnetic field strength (Tesla) (along z-axis)
E = np.array([0, 0, 0])  # Electric field strength (V/m) (no electric field for now)
dt = 1e-6  # Time step (s)
T_max = 1e-3  # Total simulation time (s)

# Initial conditions
v0 = np.array([1e5, 0, 0])  # Initial velocity (m/s)
r0 = np.array([0, 0, 0])  # Initial position (m)

# Function to compute Lorentz force
def lorentz_force(v, E, B, q):
    return q * (E + np.cross(v, B))  # Ensure cross product with 1D arrays

# Euler's method to update position and velocity
def simulate_motion(E, B, v0, r0, q, m, dt, T_max):
    time_steps = int(T_max / dt)
    r = np.zeros((time_steps, 3))
    v = np.zeros((time_steps, 3))
    
    r[0] = r0
    v[0] = v0
    
    for t in range(1, time_steps):
        F = lorentz_force(v[t-1], E, B, q)  # Call lorentz_force for each time step
        a = F / m  # Acceleration
        v[t] = v[t-1] + a * dt  # Update velocity
        r[t] = r[t-1] + v[t] * dt  # Update position
        
    return r

# Simulate the motion
trajectory = simulate_motion(E, B, v0, r0, q, m, dt, T_max)

# Plot the trajectory
plt.figure(figsize=(8, 6))
plt.plot(trajectory[:, 0], trajectory[:, 1], label="Particle Path")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Trajectory of a Particle in a Uniform Magnetic Field")
plt.grid(True)
plt.legend()
plt.show()
