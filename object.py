import numpy as np

class Body:
    def __init__(self, mass, position, velocity, name="body", color=(255, 255, 255), radius=5):
        self.mass = mass
        self.position = np.array(position, dtype=float)   # [x, y]
        self.velocity = np.array(velocity, dtype=float)   # [vx, vy]
        self.acceleration = np.zeros(2, dtype=float)      # [ax, ay] — computed each step
        self.name = name
        self.color = color
        self.radius = radius
