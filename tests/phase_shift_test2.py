# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define constants and parameters
mass = 70  # kg
step_frequency = 1  # steps per second
height = 1.75  # meters
gravity = 9.81  # m/s^2
resonance_factor = 0.5
water_content = 0.67
phase_factor_threshold = 1000  # Joules

# Function to calculate kinetic energy
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

# Function to calculate potential energy
def potential_energy(mass, height, gravity):
    return mass * height * gravity

# Function to calculate resonance energy
def resonance_energy(water_content, resonance_factor):
    return water_content * resonance_factor

# Function to calculate total energy
def total_energy(kinetic_energy, potential_energy, resonance_energy):
    return kinetic_energy + potential_energy + resonance_energy

# Simulate phase shifting over multiple iterations
iterations = 30
results = []

for i in range(iterations):
    velocity = step_frequency * height
    ke = kinetic_energy(mass, velocity)
    pe = potential_energy(mass, height, gravity)
    re = resonance_energy(water_content, resonance_factor)
    te = total_energy(ke, pe, re)
    
    phase_shift_achieved = te > phase_factor_threshold
    results.append([i+1, ke, pe, re, te, phase_shift_achieved])

# Convert results to a DataFrame
columns = ['Iteration', 'Kinetic Energy (J)', 'Potential Energy (J)', 'Resonance Energy (J)', 'Total Energy (J)', 'Phase Shift Achieved']
df = pd.DataFrame(results, columns=columns)

# Display the DataFrame
print(df)

# Visualize the results
plt.figure(figsize=(14, 6))

# Plot Total Energy per Iteration
plt.subplot(1, 2, 1)
plt.plot(df['Iteration'], df['Total Energy (J)'], marker='o')
plt.axhline(y=phase_factor_threshold, color='r', linestyle='--', label='Phase Factor Threshold')
plt.title('Total Energy per Iteration')
plt.xlabel('Iteration')
plt.ylabel('Total Energy (J)')
plt.legend()

# Plot Cumulative Phase Shifts
cumulative_phase_shifts = np.cumsum(df['Phase Shift Achieved'])
plt.subplot(1, 2, 2)
plt.plot(df['Iteration'], cumulative_phase_shifts, marker='o')
plt.title('Cumulative Phase Shifts')
plt.xlabel('Iteration')
plt.ylabel('Cumulative Phase Shifts')

plt.tight_layout()
plt.show()
