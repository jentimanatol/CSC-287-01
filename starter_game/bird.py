import pygame
import random
from pygame.sprite import Sprite

class Bird(Sprite):
    """A class to manage the bird."""

    def __init__(self, game):
        """Initialize the bird and set its starting position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load the bird images and get their rects.
        self.images = [
            pygame.image.load('C:\\BHCC\\python\\CSC-287-01\\starter_game\\assets\\bird\\bird_0.png'),
            pygame.image.load('C:\\BHCC\\python\\CSC-287-01\\starter_game\\assets\\bird\\bird_1.png')
        ]
        self.images = [pygame.transform.scale(image, (self.settings.bird_width, self.settings.bird_height)) for image in self.images]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

        # Start each new bird at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the bird's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        # Flipping flag
        self.facing_right = True

        # Timer for wing flapping
        self.last_flap_time = pygame.time.get_ticks()

    def update(self):
        """Update the bird's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.bird_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.bird_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.bird_speed
            if self.facing_right:
                self.facing_right = False
                self.image = pygame.transform.flip(self.image, True, False)
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.bird_speed
            if not self.facing_right:
                self.facing_right = True
                self.image = pygame.transform.flip(self.image, True, False)

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

        # Handle wing flapping animation
        current_time = pygame.time.get_ticks()
        if current_time - self.last_flap_time > self.settings.wing_flap_speed:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)
            self.last_flap_time = current_time

        # Check for border collisions
        if self.rect.left <= 0 or self.rect.right >= self.screen_rect.right or self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            self.settings.accidents += 1
            self.reset_position()

    def reset_position(self):
        """Reset the bird to a new random X position with a margin."""
        margin = self.settings.bird_margin
        self.x = random.randint(margin, self.screen_rect.width - self.rect.width - margin)
        self.rect.x = self.x
        self.rect.y = self.screen_rect.height // 2

    def blitme(self):
        """Draw the bird at its current location."""
        self.screen.blit(self.image, self.rect)
