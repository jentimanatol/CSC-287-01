# alien_invasion.py
import sys
import threading
import serial
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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
        self.bullets = pygame.sprite.Group()
        self.joystick_data = {'x': 0, 'y': 0, 'button': 0}
        self.previous_button_state = 0
        self.running = True
        self.last_fire_time = 0
        self.fire_cooldown = 250  # Cooldown period in milliseconds

    def run_game(self):
        """Start the main loop for the game."""
        joystick_thread = threading.Thread(target=self._read_joystick_data)
        joystick_thread.start()
        while self.running:
            self._check_events()
            self._update_ship()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
        joystick_thread.join()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

    def _read_joystick_data(self):
        """Read joystick data from the serial port."""
        ser = serial.Serial('COM3', 9600, timeout=1)
        while self.running:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8', errors='ignore').rstrip()
                parts = data.split('|')
                self.joystick_data['x'] = int(parts[0].split(':')[1].strip())
                self.joystick_data['y'] = int(parts[1].split(':')[1].strip())
                self.joystick_data['button'] = int(parts[2].split(':')[1].strip())

    def _update_ship(self):
        """Update the ship's position based on joystick data."""
        x = self.joystick_data['x']
        y = self.joystick_data['y']
        button = self.joystick_data['button']
        
        if x < 400:
            self.ship.moving_left = True
            self.ship.moving_right = False
        elif x > 600:
            self.ship.moving_right = True
            self.ship.moving_left = False
        else:
            self.ship.moving_left = False
            self.ship.moving_right = False

        if y < 400:
            self.ship.moving_up = True
            self.ship.moving_down = False
        elif y > 600:
            self.ship.moving_down = True
            self.ship.moving_up = False
        else:
            self.ship.moving_up = False
            self.ship.moving_down = False

        # Fire bullet if button is pressed and was not pressed before
        current_time = pygame.time.get_ticks()
        if button == 1 and self.previous_button_state == 0 and (current_time - self.last_fire_time) > self.fire_cooldown:
            self._fire_bullet()
            self.last_fire_time = current_time
        
        # Update the previous button state
        self.previous_button_state = button

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
