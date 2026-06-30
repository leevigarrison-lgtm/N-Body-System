import globals as g
import integrate

# get global and changable objects
globals = g.globals
changables = g.changables

def compute_iteration():
    integration_method_name = globals.integration_method_name
    bodies = changables.bodies

    integrator = getattr(integrate, integration_method_name)
    integrator.step(bodies)

    return bodies