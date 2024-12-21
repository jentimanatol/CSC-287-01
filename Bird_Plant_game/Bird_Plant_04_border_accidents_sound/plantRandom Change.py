#plant.py
#Plant location : C:\BHCC\python\CSC-287-01\starter_game\assets\plant\plant_0.png
# plant file random from : plant_0.png , plant_1.png ,,, to plant_35.png, plant_36.png.
#Plant location   C:\BHCC\python\CSC-287-01\starter_game\assets\plant\plant_36.png


import pygame
import random
from pygame.sprite import Sprite

class Plant(Sprite):
    """A class to manage the plant."""

    def __init__(self, game):
        """Initialize the plant and set its starting position."""
        super().__init__()
        self.screen = game.screen

        # Randomly select a plant image
        plant_number = random.randint(0, 36)
        self.image = pygame.image.load(f'assets\\plant\\plant_{plant_number}.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

        # Start each new plant at a random position on the screen
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = random.randint(0, self.screen_rect.height - self.rect.height)

    def blitme(self):
        """Draw the plant at its current location."""
        self.screen.blit(self.image, self.rect)
