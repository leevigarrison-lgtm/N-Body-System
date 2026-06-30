import object

# Basic Test
sun   = object.body(mass=1.989e30, position=[0, 0],        velocity=[0, 0],     name="Sun",   color=(255,220,50))
earth = object.body(mass=5.972e24, position=[1.496e11, 0],  velocity=[0, 29780], name="Earth", color=(50,150,255))

# Objects defined BEFORE first frame
class global_objects():
    def __init__(self):
        self.DIMENSION   = 2         # 2D simulation (3D requires minimal changes — just swap np.zeros(2) to np.zeros(3))
        self.G           = 6.674e-11 # gravitational constant (SI units — meters, kg, seconds)
        self.dt = 3600
        self.integration_method_name = "euler"
        self.softening = 1e6
        self.ui_panel_width = 300
        self.screen_width = 600 + self.ui_panel_width
        self.screen_height = 600


# Objects defined AFTER first frame. These objects can change during the sim to see different effectss
class changeable_objects():
    def __init__(self):
        self.bodies = [sun, earth]
        self.fps = 60

changables = changeable_objects()
globals = global_objects()