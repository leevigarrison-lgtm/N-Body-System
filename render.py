import pygame
import pygame_gui
import globals as g
import simulate
import screen_manager
import ui_manager


# Get Real-Time Change and Global Objects:

globals = g.globals
globals_default = g.copy_globals # Store the original values (modified by MenuUI accordingly)

# Scree Manager Calls
screen_settings = screen_manager.base
screen_functions = screen_manager.screen_functions

# UI Manager Calls
ui_base = ui_manager.base

running = True
while running:
    # 1. Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Button Events:
        if event.type == pygame_gui.UI_BUTTON_PRESSED:

            # Pause Button
            if event.ui_element == ui_base.pause_button:

                if ui_base.pause_button.text == "Pause":
                    globals.dt = 0
                    ui_base.pause_button.set_text("Continue")
                    ui_base.dt_text.set_text("0")
                else:
                    globals.dt = globals_default.dt
                    ui_base.pause_button.set_text("Pause")
                    ui_base.dt_text.set_text(str(globals_default.dt))

            # Restart Button (broken rn idk y)
            if event.ui_element == ui_base.restart_button:
                globals = globals_default

            if event.ui_element == ui_base.restart_button:
                globals = globals_default

        # Text Boxes
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:

            if event.ui_element == ui_base.dimension_text:
                try:
                    globals.DIMENSION = float(ui_base.dimension_text.get_text())
                except ValueError:
                    globals.DIMENSION = globals_default.DIMENSION
                    ui_base.dimension_text.set_text(str(globals_default.DIMENSION))

            if event.ui_element == ui_base.grav_constant_text:
                try:
                    globals.G = float(ui_base.grav_constant_text.get_text())
                    globals_default.G = float(ui_base.grav_constant_text.get_text())
                except ValueError:
                    globals.G = globals_default.G
                    ui_base.grav_constant_text.set_text(str(globals_default.G))


            if event.ui_element == ui_base.dt_text:
                try:
                    globals.dt = float(ui_base.dt_text.get_text())
                    globals_default.dt = float(ui_base.dt_text.get_text())
                except ValueError:
                    globals.dt = globals_default.dt
                    #globals_default.dt = globals_default.dt

                    ui_base.dt_text.set_text(str(globals_default.dt))

            if event.ui_element == ui_base.menu_percent_text:
                try:
                    globals.menu_screen_percentage = float(ui_base.menu_percent_text.get_text())
                    globals_default.menu_screen_percentage = float(ui_base.menu_percent_text.get_text())

                    # Resize the screen first
                    adjusted_screen_width = globals.screen_width_and_height * (1 + globals.menu_screen_percentage)
                    screen_settings.screen = pygame.display.set_mode((adjusted_screen_width, globals.screen_width_and_height))

                    ui_base.reset()
                except ValueError:
                    ui_base.menu_percent_text.set_text(str(globals_default.menu_screen_percentage))

            

                
                

        ui_base.manager.process_events(event)

    # 2. Update state (nothing yet)

    # 3. Draw

    # Screen Background Black:
    screen_settings.screen.fill((0, 0, 0))

    # Create Bodies as different circles: (All same size for now)

    simulate.compute_iteration()

    for body in globals.bodies:
        body_scaled_properties = screen_functions.position_to_screen(body)
        pygame.draw.circle(screen_settings.screen, body.color, body_scaled_properties["position"], 20)
    
    # Display UI
    time_delta = screen_settings.clock.tick(globals.fps) / 1000.0
    ui_base.manager.update(time_delta)

    ui_base.manager.draw_ui(screen_settings.screen)

    # Display bodies
    pygame.display.flip()

    # Change FPS with changable FPS in settings
    screen_settings.clock.tick(globals.fps) 

pygame.quit()