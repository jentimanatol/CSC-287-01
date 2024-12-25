class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.5  # Start at minimum ship speed

        # Bullet settings
        self.bullet_speed = 1.0  # Start at minimum bullet speed
        self.bullet_width = 3  # Standard bullet width
        self.bullet_height = 15  # Standard bullet height
        self.bullet_color = (60, 60, 60)  # Bullet color
        self.bullets_allowed = 3  # Maximum number of bullets allowed

        # Enemy ship settings
        self.enemy_speed = 0.5  # Start at minimum enemy ship speed

        # Enemy bullet settings
        self.enemy_bullet_speed = 1.0  # Start at minimum enemy bullet speed
        self.enemy_bullet_interval = 3000  # Start at maximum interval for easiest difficulty (3000 milliseconds)
