# alien_invasion.py
import sys
import threading
import serial
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from enemy_ship import EnemyShip
from enemy_bullet import EnemyBullet

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
        self.enemy_ships = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.joystick_data = {'x': 0, 'y': 0, 'button': 0}
        self.previous_button_state = 0
        self.running = True
        self.last_fire_time = 0
        self.fire_cooldown = 100  # Decreased cooldown period in milliseconds

        # Create enemy ships
        for _ in range(3):  # Add 3 enemy ships
            enemy_ship = EnemyShip(self)
            self.enemy_ships.add(enemy_ship)

    def run_game(self):
        """Start the main loop for the game."""
        self.joystick_thread = threading.Thread(target=self._read_joystick_data)
        self.joystick_thread.start()
        while self.running:
            self._check_events()
            self._update_ship()
            self.ship.update()
            self._update_bullets()
            self._update_enemy_ships()
            self._update_enemy_bullets()
            self._check_collisions()
            self._update_screen()
            self._debug_ship_position()  # Add debug statement
            self.clock.tick(60)
        self.joystick_thread.join()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()

    def _read_joystick_data(self):
        """Read joystick data from the serial port."""
      #  ser = serial.Serial('COM3', 9600, timeout=1)
        ser = serial.Serial('COM5', 9600, timeout=1)
        while self.running:
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8', errors='ignore').rstrip()
                parts = data.split('|')
                self.joystick_data['x'] = int(parts[0].split(':')[1].strip())
                self.joystick_data['y'] = int(parts[1].split(':')[1].strip())
                self.joystick_data['button'] = int(parts[2].split(':')[1].strip())
                print(f"Joystick data read: {self.joystick_data}")  # Debug statement

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

        # Fire bullet if button is not pressed and cooldown period has passed
        current_time = pygame.time.get_ticks()
        if button == 0 and (current_time - self.last_fire_time) > self.fire_cooldown:
            self._fire_bullet()
            self.last_fire_time = current_time
        
        # Update the previous button state
        self.previous_button_state = button

        # Debug statement to check joystick data
        print(f"Joystick data: x={x}, y={y}, button={button}")

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for bullet-enemy collisions
        collisions = pygame.sprite.groupcollide(self.bullets, self.enemy_ships, True, False)
        for enemy_ship in collisions.values():
            for ship in enemy_ship:
                ship.reset_position()

    def _update_enemy_ships(self):
        """Update the positions of all enemy ships."""
        self.enemy_ships.update()

    def _update_enemy_bullets(self):
        """Update the positions of all enemy bullets."""
        self.enemy_bullets.update()
        for bullet in self.enemy_bullets.copy():
            if bullet.rect.top >= self.settings.screen_height:
                self.enemy_bullets.remove(bullet)

    def _check_collisions(self):
        """Check for collisions between the ship and enemy bullets."""
        if pygame.sprite.spritecollideany(self.ship, self.enemy_bullets):
            self._game_over()

    def _game_over(self):
        """Handle the game over condition."""
        self.running = False
        print("Game Over! Restarting...")
        self.joystick_thread.join()  # Wait for the joystick thread to finish
        self._reset_game()  # Call the reset method

    def _reset_game(self):
        """Reset the game state."""
        self.ship.center_ship()  # Center the ship
        print(f"Ship centered at: x={self.ship.x}, y={self.ship.y}")  # Debug statement
        self.bullets.empty()  # Clear all bullets
        self.enemy_bullets.empty()  # Clear all enemy bullets
        self.last_fire_time = 0  # Reset the firing state
        self.previous_button_state = 0  # Reset the button state
        self.joystick_data = {'x': 512, 'y': 512, 'button': 0}  # Reset joystick data to center
        print(f"Joystick data reset to: {self.joystick_data}")  # Debug statement

        # Restart the joystick thread
        self.joystick_thread = threading.Thread(target=self._read_joystick_data)
        self.joystick_thread.start()
        self.running = True  # Restart the game loop

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.enemy_bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        for enemy_ship in self.enemy_ships.sprites():
            enemy_ship.blitme()
        pygame.display.flip()

    def _debug_ship_position(self):
        """Print the ship's position and movement flags for debugging."""
        print(f"Ship position: x={self.ship.x}, y={self.ship.y}")
        print(f"Moving right: {self.ship.moving_right}, Moving left: {self.ship.moving_left}")
        print(f"Moving up: {self.ship.moving_up}, Moving down: {self.ship.moving_down}")

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
