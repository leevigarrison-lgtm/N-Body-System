import globals as g
import numpy as np

globals = g.globals

# define commonly used variables globally for simpicity
grav_constant = globals.G
dt = globals.dt

class compute:

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
                    
                    potential += -(grav_constant * m_i.mass * m_j.mass) / r_ij_magnitude
        
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
    