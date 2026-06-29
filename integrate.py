import numpy as np
from globals import G
from globals import DT_DEFAULT
from object import body
import copy

class compute_acceleration:
    # O(n^2) complexity

    # The mass i feels the acceleration from every other body.
    def step(bodies):
        for m_i in bodies:
            a_i = np.zeros(2, dtype=float)
            
            for m_j in bodies:

                # i != j in N-Body Sum
                if m_i != m_j:

                    # Vector Distance
                    r_ij = m_j.position - m_i.position

                    # Magnitude and Unit Vector Calculations
                    r_ij_magnitude = np.linalg.norm(r_ij)
                    r_ij_magnitude_squared = r_ij_magnitude ** 2
                    r_ij_unit = r_ij / r_ij_magnitude

                    # Complete Scalar
                    scalar = ((G * m_j.mass)/r_ij_magnitude_squared)

                    # Calculation
                    a_i += scalar * r_ij_unit

            m_i.acceleration = a_i

# This is the most inaccurate numerical integration class.
# This assumes a constant rate of change because it's a first-order integrator.
# The error term grows extremely fast because it's neglecting second-order corrections

class euler:
    def step(bodies):
        # O(n^2):
        compute_acceleration.step(bodies)

        for m in bodies:

            # Position function
            m.position = m.position + (m.velocity * DT_DEFAULT)

            # Velocity function:
            m.velocity = m.velocity + (m.acceleration * DT_DEFAULT)

# Similar to Euler. Uses a second order average correction to reduce error significatly (factor of 4 since error grows x^2 on Euler)
# Energy conservation is much better.
class improved_euler:
    def step(bodies):
        bodies_copy = copy.deepcopy(bodies) # For prediction value

        # Reuse Euler without rewriting code:
        euler.step(bodies_copy) # Compute Euler on the copied array

        # Update using average of 2 values:

        # Uses index instead of values immediately.
        for i in range(len(bodies)):
            m_actual = bodies[i]
            m_predicted = bodies_copy[i]

            # Position function
            m_actual.position = m_actual.position + ((m_actual.velocity + m_predicted.velocity) * 0.5 * DT_DEFAULT)

            # Velocity function:
            m_actual.velocity = m_actual.velocity + ((m_actual.acceleration + m_predicted.acceleration) * 0.5 * DT_DEFAULT)

# This is what's actually used in orbital mechanics
# The energy conservation error oscillates instead of accumulating in a destructive way.
# This is still a second-order correction, so it's not any more accurate than improved_euler.
# All mechanics are intertwined instead of seperate.

class velocity_verlet:
    def step(bodies):
        compute_acceleration.step(bodies)

        # Array for saving old accelerations
        acc = []

        # Compute new position:
        for m in bodies:
            m.position = (m.position + m.velocity * DT_DEFAULT) + (0.5 * m.acceleration * DT_DEFAULT**2)
            acc.append(m.acceleration)

        # Compute new acceleration
        compute_acceleration.step(bodies)

        # Uses old and new accelerations to update velocity.
        for i in range(len(bodies)):
            bodies[i].velocity = bodies[i].velocity + (0.5 * (bodies[i].acceleration + acc[i]) * DT_DEFAULT)

class energy:

    # Computes E_0 (initial energy of the system for ratio calculation)
    def __init__(self, bodies):
        self.bodies = bodies
        self.initial_energy = self.compute_total_energy(bodies)

    # KE = 1/2 m v^2
    # KE is the energy for motion
    # Total KE is calculated by the sum of all the KEs.
    def total_kinetic(self):
        kinetic = 0

        for m in self.bodies:
            kinetic += 0.5 * m.mass * np.dot(m.velocity, m.velocity)

        return kinetic

    # This is the gravitational PE.
    # Basically calculates the PE of all of the bodies across there relationships, not just one body.
    def total_potential(self):
        potential = 0

        # Only need the relationship between objects, not everything like in compute_acceleration()
        for i in range(len(self.bodies)):
            for j in range(i + 1, len(self.bodies)):
                m_i = self.bodies[i]
                m_j = self.bodies[j]

                # Remove the possibility of m_i being m_j (infinite distance problem)
                
                if m_i != m_j:
                    r_ij = m_j.position - m_i.position
                    r_ij_magnitude = np.linalg.norm(r_ij)
                    
                    potential += -(G * m_i.mass * m_j.mass) / r_ij_magnitude
        
        return potential
    
    def compute_total_energy(self):
        kinetic = self.total_kinetic()
        potential = self.total_potential()

        # Total energy of a system determined by the sum of KE and PE.
        return kinetic + potential
    
    # Ratio of energy conserved.
    def compute_energy_conservation_ratio(self):
        E_t = self.compute_energy_conservation()
        E_0 = self.initial_energy
        E_0_abs = abs(E_0)

        return (E_t - E_0) / E_0_abs
    