# enemy_ship.py


import pygame
import random
from enemy_bullet import EnemyBullet

class EnemyShip(pygame.sprite.Sprite):
    """A class to manage enemy ships."""

    def __init__(self, ai_game):
        """Initialize the enemy ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.ai_game = ai_game

        # Load the enemy ship image and get its rect.
        self.image = pygame.image.load('images/enemy_ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new enemy ship at a random position at the top of the screen.
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = self.screen_rect.top

        # Store a float for the enemy ship's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's moving randomly.
        self.moving_right = random.choice([True, False])
        self.moving_down = True

        # Bullet firing timer
        self.last_fire_time = pygame.time.get_ticks()

    def update(self):
        """Update the enemy ship's position."""
        # Move the ship randomly.
        if self.moving_right:
            self.x += self.settings.enemy_speed
            if self.rect.right >= self.screen_rect.right:
                self.moving_right = False
        else:
            self.x -= self.settings.enemy_speed
            if self.rect.left <= 0:
                self.moving_right = True

        self.y += self.settings.enemy_speed
        if self.rect.bottom >= self.screen_rect.bottom:
            self.reset_position()

        # Update rect object from self.x and self.y.
        self.rect.x = self.x
        self.rect.y = self.y

        # Fire bullet every 2 seconds
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fire_time > self.settings.enemy_bullet_interval:
            self.fire_bullet()
            self.last_fire_time = current_time

    def blitme(self):
        """Draw the enemy ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def reset_position(self):
        """Reset the enemy ship to a new random position at the top of the screen."""
        self.rect.x = random.randint(0, self.screen_rect.width - self.rect.width)
        self.rect.y = self.screen_rect.top
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def fire_bullet(self):
        """Fire a bullet from the enemy ship."""
        new_bullet = EnemyBullet(self.ai_game, self)
        self.ai_game.enemy_bullets.add(new_bullet)
