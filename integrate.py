import numpy as np
from compute_acceleration import compute
import copy

import globals as g

globals = g.globals

# define commonly used variables globally for simpicity


# This is the most inaccurate numerical integration class.
# This assumes a constant rate of change because it's a first-order integrator.
# The error term grows extremely fast because it's neglecting second-order corrections

class euler:
    def step(bodies):

        # Need to define globals here since dt and grav_constant is dynamical
        dt = globals.dt

        # O(n^2):
        compute.step(bodies)

        for m in bodies:

            # Position function
            m.position = m.position + (m.velocity * dt)

            # Velocity function:
            m.velocity = m.velocity + (m.acceleration * dt)

# Similar to Euler. Uses a second order average correction to reduce error significatly (factor of 4 since error grows x^2 on Euler)
# Energy conservation is much better.
class improved_euler:
    def step(bodies):
        # Need to define globals here since dt and grav_constant is dynamical
        dt = globals.dt

        bodies_copy = copy.deepcopy(bodies) # For prediction value

        # Reuse Euler without rewriting code:
        euler.step(bodies_copy) # Compute Euler on the copied array

        # Update using average of 2 values:

        # Uses index instead of values immediately.
        for i in range(len(bodies)):
            m_actual = bodies[i]
            m_predicted = bodies_copy[i]

            # Position function
            m_actual.position = m_actual.position + ((m_actual.velocity + m_predicted.velocity) * 0.5 * dt)

            # Velocity function:
            m_actual.velocity = m_actual.velocity + ((m_actual.acceleration + m_predicted.acceleration) * 0.5 * dt)

# This is what's actually used in orbital mechanics
# The energy conservation error oscillates instead of accumulating in a destructive way.
# This is still a second-order correction, so it's not any more accurate than improved_euler.
# All mechanics are intertwined instead of seperate.

class velocity_verlet:
    def step(bodies):

        # Need to define globals here since dt and grav_constant is dynamical
        dt = globals.dt
        compute.step(bodies)

        # Array for saving old accelerations
        acc = []

        # Compute new position:
        for m in bodies:
            m.position = (m.position + m.velocity * dt) + (0.5 * m.acceleration * dt**2)
            acc.append(m.acceleration)

        # Compute new acceleration
        compute.step(bodies)

        # Uses old and new accelerations to update velocity.
        for i in range(len(bodies)):
            bodies[i].velocity = bodies[i].velocity + (0.5 * (bodies[i].acceleration + acc[i]) * dt)