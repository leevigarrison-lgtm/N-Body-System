import globals as g
import integrate

# get global and changable objects
globals = g.globals

def compute_iteration():
    integration_method_name = globals.integration_method_name
    bodies = globals.bodies

    integrator = getattr(integrate, integration_method_name)
    integrator.step(bodies)

    return bodies