import pygame
import sys
from settings import Settings
from bird import Bird
from plant import Plant

class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.score = 0

        # Set the screen height and caption.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Bird/Plant Game!")

        self.bird = Bird(self)
        self.plant = Plant(self)

        # Set a timer event for updating the plant image every second
        self.PLANT_UPDATE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.PLANT_UPDATE_EVENT, 1000)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.bird.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == self.PLANT_UPDATE_EVENT:
                self.plant.update_image()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.bird.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.bird.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.bird.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.bird.moving_right = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.bird.moving_up = False
        if event.key == pygame.K_DOWN:
            self.bird.moving_down = False
        if event.key == pygame.K_LEFT:
            self.bird.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.bird.moving_right = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.bird.blitme()
        self.plant.blitme()
        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
