import pygame 

class Pig():

    def __init__(self, screen):
        """Initialize the pig and set its starting position."""
        self.screen = screen

        # Load the pig image and set pig and screen to rect.
        self.image = pygame.image.load('pig.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the pig at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Speed of the pig
        self.pig_speed = 1.5
        self.center = float(self.pig_speed)

        # Set a variable for each movement.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.direction = ['right', 'left']

    def update(self):
        """Update the position of the pig."""

        if self.rect.right <= self.screen_rect.right:
            if self.moving_right:
                self.rect.centerx += self.pig_speed

        if self.rect.left > 0:
            if self.moving_left:
                self.rect.centerx -= self.pig_speed

        if self.rect.top > 0:
            if self.moving_up:
                self.rect.bottom -= self.pig_speed

        if self.rect.bottom <= self.screen_rect.bottom:
            if self.moving_down:
                self.rect.bottom += self.pig_speed

    def blitme(self):
        """Draw the pig at its current location."""
        self.screen.blit(self.image, self.rect)