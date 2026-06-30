import numpy as np
import pygame
import pygame_gui
import globals as g

globals = g.globals
changables = g.changables

bodies = changables.bodies
screen_width = globals.screen_width
screen_height = globals.screen_height

# Call base pygame function
pygame.init()

# Screen class to call globally
class base_screen():
    def __init__(self):
        # get norm factor. If #bodies = 0, prevent crashing by exiting.
        self.norm_factor = to_screen.get_norm_constants() 
        self.display_info = pygame.display.Info()      
        self.screen = pygame.display.set_mode((screen_width, screen_height)) 
        self.clock = pygame.time.Clock()

# Class to convert massive orbital mechanics values into pixels for display.
class to_screen():
    # Truncate Each Bodies Position to Fit Screen:
    # Uses Distance Between Object's StartPositions as the variable Truncate Factor

    @staticmethod
    def get_norm_constants():

        # Gets max distance from origin

        max_distance = 0

        if len(bodies) <= 1:
            return None

        for m_i in bodies:
            magnitude = np.linalg.norm(m_i.position)

            if magnitude > max_distance:
                max_distance = magnitude
        
        # 10% more to make look more natural
        max_distance = max_distance * 1.1

        screen_size_constant_x = ((screen_width - globals.ui_panel_width) / 2) / max_distance
        screen_size_constant_y = (screen_height / 2) / max_distance

        return [screen_size_constant_x, screen_size_constant_y]
    
    @staticmethod
    def position_to_screen(body):
        # Scale using norm factor calculated above.

        position = body.position

        center_x = (screen_width - globals.ui_panel_width) / 2
        center_y = screen_height/2

        # Multiply by -1 for the vertical "flip:" (pygames has inverted coordinates)
        # Add center_x and center_y to corresponding values because pygame's (0,0) starts at the top left
        # Convert to int because pygame only accepts int values for drawing
        new_position = np.array([int((position[0] * base.norm_factor[0]) + center_x), int(-(position[1] * base.norm_factor[1]) + center_y)])

        return_dict = {
            "position": new_position,
        }

        return return_dict
    
base = base_screen()
screen_functions = to_screen()

if base.norm_factor is None:
    print("Cannot run simulation since no bodies are defined!")
    exit()