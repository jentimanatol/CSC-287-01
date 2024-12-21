# settings.py

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 3.0  # Increased speed

        # Bullet settings
        self.bullet_speed = 5.0  # Increased bullet speed
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Enemy ship settings
        self.enemy_speed = 1.0

        # Enemy bullet settings
        self.enemy_bullet_speed = 3.0
        self.enemy_bullet_interval = 2000  # Fire every 2 seconds (2000 milliseconds)
