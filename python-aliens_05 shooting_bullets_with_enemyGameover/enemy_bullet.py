# enemy_bullet.py
import pygame
from pygame.sprite import Sprite

class EnemyBullet(Sprite):
    """A class to manage bullets fired by enemy ships."""

    def __init__(self, ai_game, enemy_ship):
        """Create a bullet object at the enemy ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = (255, 0, 0)  # Red color for enemy bullets

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = enemy_ship.rect.midbottom

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet down the screen."""
        # Update the exact position of the bullet.
        self.y += self.settings.enemy_bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
