import pygame
import random
from pygame.sprite import Sprite

class Plant(Sprite):
    """A class to manage the plant."""

    def __init__(self, game):
        """Initialize the plant and set its starting position."""
        super().__init__()
        self.screen = game.screen

        # Load the initial plant image
        self.image = pygame.image.load('assets\\plant\\plant_0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

        # Start the plant at the middle bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def update_image(self):
        """Update the plant image to a random shape."""
        plant_number = random.randint(1, 35)
        self.image = pygame.image.load(f'assets\\plant\\plant_{plant_number}.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the plant at its current location."""
        self.screen.blit(self.image, self.rect)
