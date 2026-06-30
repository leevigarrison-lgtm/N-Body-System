import pygame
import pygame_gui
import globals as g
import simulate
import screen_manager
import ui_manager


# Get Real-Time Change and Global Objects:

globals = g.globals
changables = g.changables

# Scree Manager Calls
screen_settings = screen_manager.base
screen_functions = screen_manager.screen_functions

# UI Manager Calls
ui_settings = ui_manager.base

running = True
while running:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame_gui.UI_BUTTON_PRESSED:
        #     if event.ui_element == button:
        #         DT_DEFAULT = 0

        ui_settings.manager.process_events(event)

    # 2. Update state (nothing yet)

    # 3. Draw

    # Screen Background Black:
    screen_settings.screen.fill((0, 0, 0))

    # Create Bodies as different circles: (All same size for now)

    simulate.compute_iteration()

    for body in changables.bodies:
        body_scaled_properties = screen_functions.position_to_screen(body)
        pygame.draw.circle(screen_settings.screen, body.color, body_scaled_properties["position"], 20)
    
    # Display UI
    ui_settings.manager.update(changables.fps)
    ui_settings.manager.draw_ui(screen_settings.screen)

    # Display bodies
    pygame.display.flip()

    # Change FPS with changable FPS in settings
    screen_settings.clock.tick(changables.fps) 

pygame.quit()