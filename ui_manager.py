import pygame
import pygame_gui
import globals as g
# Need screen manager to run first because of pygame
import screen_manager

globals = g.globals

class create_ui:
    def __init__(self):
        
        screen_width_and_height = globals.screen_width_and_height
        adjusted_screen_width = screen_width_and_height * (1 + globals.menu_screen_percentage)

        self.manager = pygame_gui.UIManager((adjusted_screen_width, screen_width_and_height))
        self.construct_ui()


    def construct_ui(self):

        screen_width_and_height = globals.screen_width_and_height
        menu_screen_percentage = globals.menu_screen_percentage

        
        adjusted_screen_width = screen_width_and_height * (1 + globals.menu_screen_percentage)
        ui_panel_width = adjusted_screen_width - screen_width_and_height
        # Create UI

        # Base Panel and Title Calls:

        self.main_panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(screen_width_and_height, 0, ui_panel_width, screen_width_and_height),
            manager=self.manager
        )

        self.main_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 0, ui_panel_width, screen_width_and_height * (1/12)),  # x, y, width, height
            text="Main Menu",
            manager=self.manager,
            container=self.main_panel
        )

        # Sim Commands:

        self.sim_options_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (1/12), ui_panel_width, screen_width_and_height * (1/24)),  # x, y, width, height
            text="Sim Commands:",
            manager=self.manager,
            container=self.main_panel
        )

        self.pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0, screen_width_and_height * (1/8), ui_panel_width, screen_width_and_height * (1/24)),
            text="Pause",
            manager=self.manager,
            container=self.main_panel
        )

        self.restart_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0, screen_width_and_height * (1/6), ui_panel_width, screen_width_and_height * (1/24)),
            text="Restart",
            manager=self.manager,
            container=self.main_panel
        )

        # Sim Settings

        self.settings_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (5/24), ui_panel_width, screen_width_and_height * (1/24)),  # x, y, width, height
            text="Simulation Settings:",
            manager=self.manager,
            container=self.main_panel
        )

        self.dimension_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (1/4), ui_panel_width * (1/4), screen_width_and_height * (1/24)),  # x, y, width, height
            text="Dimension: ",
            manager=self.manager,
            container=self.main_panel
        )

        self.dimension_text = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(ui_panel_width * (1/4), screen_width_and_height * (1/4), ui_panel_width * (7/10), screen_width_and_height * (1/24)),
            manager=self.manager,
            container=self.main_panel
        )
        self.dimension_text.set_text(str(globals.DIMENSION))



        self.grav_constant_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (7/24), ui_panel_width * (1/4), screen_width_and_height * (1/24)),  # x, y, width, height
            text="G-Constant: ",
            manager=self.manager,
            container=self.main_panel
        )

        self.grav_constant_text = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(ui_panel_width * (1/4), screen_width_and_height * (7/24), ui_panel_width * (7/10), screen_width_and_height * (1/24)),
            manager=self.manager,
            container=self.main_panel
        )
        self.grav_constant_text.set_text(str(globals.G))


        self.dt_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (1/3), ui_panel_width * (1/4), screen_width_and_height * (1/24)),  # x, y, width, height
            text="Delta Time:",
            manager=self.manager,
            container=self.main_panel
        )

        self.dt_text = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(ui_panel_width * (1/4), screen_width_and_height * (1/3), ui_panel_width * (7/10), screen_width_and_height * (1/24)),
            manager=self.manager,
            container=self.main_panel
        )
        self.dt_text.set_text(str(globals.dt))


        self.fps_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (3/8), ui_panel_width * (1/4), screen_width_and_height * (1/24)),  # x, y, width, height
            text="FPS:",
            manager=self.manager,
            container=self.main_panel
        )

        self.fps_text = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(ui_panel_width * (1/4), screen_width_and_height * (3/8), ui_panel_width * (7/10), screen_width_and_height * (1/24)),
            manager=self.manager,
            container=self.main_panel
        )
        self.fps_text.set_text(str(globals.fps))

        self.integration_method_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (5/12), ui_panel_width * (1/4), screen_width_and_height * (1/24)),  # x, y, width, height
            text="Integration: ",
            manager=self.manager,
            container=self.main_panel
        )

        self.integration_method_dropdown = pygame_gui.elements.UIDropDownMenu(
            options_list=["euler", "improved_euler", "velocity_verlet"],
            starting_option=globals.integration_method_name,
            relative_rect=pygame.Rect(ui_panel_width * (1/4), screen_width_and_height * (5/12), ui_panel_width * (7/10), screen_width_and_height * (1/24)),
            container=self.main_panel,
            manager=self.manager
        )

        self.bodies_selection_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (11/24), ui_panel_width * (1/4), screen_width_and_height * (1/24)),  # x, y, width, height
            text="Select Set: ",
            manager=self.manager,
            container=self.main_panel
        )

        # Will read a .csv file based on presets, or custom sets with specific names
        self.bodies_selection_text = pygame_gui.elements.UIDropDownMenu(
            options_list=["Test"],
            starting_option="Test",
            relative_rect=pygame.Rect(ui_panel_width * (1/4), screen_width_and_height * (11/24), ui_panel_width * (7/10), screen_width_and_height * (1/24)),
            container=self.main_panel,
            manager=self.manager
        )


        # Screen Settings:

        self.sim_properties_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (1/2), ui_panel_width, screen_width_and_height * (1/24)),  # x, y, width, height
            text="Screen Settings:",
            manager=self.manager,
            container=self.main_panel
        )



        self.screen_dim_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (13/24), ui_panel_width * (1/4), screen_width_and_height * (1/24)),  # x, y, width, height
            text="Sim Size:",
            manager=self.manager,
            container=self.main_panel
        )

        self.screen_dim_text = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(ui_panel_width * (1/4), screen_width_and_height * (13/24), ui_panel_width * (7/10), screen_width_and_height * (1/24)),
            manager=self.manager,
            container=self.main_panel
        )
        self.screen_dim_text.set_text(str(screen_width_and_height))



        self.menu_percent_title = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, screen_width_and_height * (7/12), ui_panel_width * (1/4), screen_width_and_height * (1/24)),  # x, y, width, height
            text="Menu %:",
            manager=self.manager,
            container=self.main_panel
        )

        self.menu_percent_text = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(ui_panel_width * (1/4), screen_width_and_height * (7/12), ui_panel_width * (7/10), screen_width_and_height * (1/24)),
            manager=self.manager,
            container=self.main_panel
        )
        self.menu_percent_text.set_text(str(globals.menu_screen_percentage))

        # # Statistical UI:


        # statistics_title = pygame_gui.elements.UILabel(
        #     relative_rect=pygame.Rect(0, 325, ui_panel_width, 50),  # x, y, width, height
        #     text="Statistics:",
        #     manager=self.manager,
        #     container=main_panel
        # )

        # energy_conservation_stats_button = pygame_gui.elements.UIButton(
        #     relative_rect=pygame.Rect(0, 375, ui_panel_width, 25),
        #     text="View Energy Conservation Stats",
        #     manager=self.manager,
        #     container=main_panel
        # )

    def reset(self):
        self.manager.clear_and_reset()
        screen_width_and_height = globals.screen_width_and_height
        adjusted_screen_width = screen_width_and_height * (1 + globals.menu_screen_percentage)
        self.manager = pygame_gui.UIManager((adjusted_screen_width, screen_width_and_height))
        self.construct_ui()

base = create_ui()