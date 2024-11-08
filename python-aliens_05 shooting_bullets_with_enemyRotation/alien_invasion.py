# alien_invasion.py
import sys
import threading
import pygame
from settings import Settings
from ship import Ship
from joystick import read_joystick_data

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.joystick_data = {'x': 0, 'y': 0, 'button': 0}
        self.running = True

    def run_game(self):
        """Start the main loop for the game."""
        self.joystick_thread = threading.Thread(target=read_joystick_data, args=(self,))
        self.joystick_thread.start()
        while self.running:
            print("Game loop running...")  # Debug statement
            self._check_events()
            self._update_ship()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
        self.joystick_thread.join()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

    def _update_ship(self):
        """Update the ship's position based on joystick data."""
        x = self.joystick_data['x']
        y = self.joystick_data['y']
        button = self.joystick_data['button']
        
        # Define dead zone range
        dead_zone = 100

        if x < (512 - dead_zone):
            self.ship.moving_left = True
            self.ship.moving_right = False
        elif x > (512 + dead_zone):
            self.ship.moving_right = True
            self.ship.moving_left = False
        else:
            self.ship.moving_left = False
            self.ship.moving_right = False

        if y < (512 - dead_zone):
            self.ship.moving_up = True
            self.ship.moving_down = False
        elif y > (512 + dead_zone):
            self.ship.moving_down = True
            self.ship.moving_up = False
        else:
            self.ship.moving_up = False
            self.ship.moving_down = False

        # Debug statements to check movement flags
        print(f"Moving left: {self.ship.moving_left}, Moving right: {self.ship.moving_right}")
        print(f"Moving up: {self.ship.moving_up}, Moving down: {self.ship.moving_down}")

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        print("Updating screen...")  # Debug statement
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
