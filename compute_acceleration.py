import numpy as np
import globals as g
from object import body
import copy

globals = g.globals

class compute:
    # O(n^2) complexity

    # The mass i feels the acceleration from every other body.
    def step(bodies):

        grav_constant = globals.G

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
                    scalar = ((grav_constant * m_j.mass)/r_ij_magnitude_squared)

                    # Calculation
                    a_i += scalar * r_ij_unit

            m_i.acceleration = a_i
