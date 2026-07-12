import object
import copy

# Basic Test
sun   = object.body(mass=1.989e30, position=[0, 0],        velocity=[0, 0],     name="Sun",   color=(255,220,50))
earth = object.body(mass=5.972e24, position=[1.496e11, 0],  velocity=[0, 29780], name="Earth", color=(50,150,255))

# Objects defined BEFORE first frame. They remain dynamical for simulation purposes.
class global_objects():
    def __init__(self):
        self.DIMENSION   = 2         # 2D simulation (3D requires minimal changes — just swap np.zeros(2) to np.zeros(3))
        self.G           = 6.674e-11 # gravitational constant (SI units — meters, kg, seconds)
        self.dt = 3600
        self.integration_method_name = "velocity_verlet"
        self.softening = 1e6
        self.screen_width_and_height = 800
        self.menu_screen_percentage = 0.6
        self.bodies = [sun, earth]
        self.fps = 360


globals = global_objects()
copy_globals = copy.deepcopy(globals)