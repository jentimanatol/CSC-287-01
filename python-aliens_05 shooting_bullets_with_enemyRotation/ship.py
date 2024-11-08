import pygame
import math

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect.
        self.original_image = pygame.image.load('images/ship.bmp')
        self.image = self.original_image
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Rotation and speed
        self.angle = 0
        self.speed = 0

    def update(self):
        """Update the ship's position based on movement flags."""
        # Rotate the ship
        if self.moving_right:
            self.angle -= self.settings.ship_rotation_speed
        if self.moving_left:
            self.angle += self.settings.ship_rotation_speed

        # Ensure the angle stays within 0-360 degrees
        self.angle %= 360

        # Move the ship forward and backward
        if self.moving_up:
            self.speed = self.settings.ship_speed
        elif self.moving_down:
            self.speed = -self.settings.ship_speed
        else:
            self.speed = 0

        # Calculate new position
        self.x += self.speed * math.cos(math.radians(self.angle))
        self.y -= self.speed * math.sin(math.radians(self.angle))

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

        # Rotate the image
        self.image = pygame.transform.rotate(self.original_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Debug statement to check the ship's angle
        print(f"Ship angle: {self.angle}")

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
