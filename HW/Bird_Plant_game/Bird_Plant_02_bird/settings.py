class Settings:
    """A class to store all game settings."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bird_speed = 3

        # Bird settings
        self.bird_width = 50
        self.bird_height = 50
        self.wing_flap_speed = 200  # Time in milliseconds between wing flaps
