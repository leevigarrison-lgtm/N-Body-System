import pygame
import pygame_gui
import screen_manager
import globals as g


globals = g.globals
changables = g.changables

class create_ui:
    def __init__(self):
        self.manager = pygame_gui.UIManager((globals.screen_width, globals.screen_height))

base = create_ui()

# Create UI
button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(10, 10, 120, 40),  # x, y, width, height
    text="Pause",
    manager=base.manager
)