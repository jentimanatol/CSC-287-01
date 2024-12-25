import sys
import threading
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from enemy_ship import EnemyShip
from enemy_bullet import EnemyBullet
from arduino_user import ArduinoUser
from pc_user import PCUser
from start_screen import StartScreen

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

        self.start_screen = StartScreen(self)
        self.ship1 = Ship(self)
        self.ship2 = Ship(self)
        self.ship2.rect.y += 100  # Adjust starting position for the second ship
        self.bullets = pygame.sprite.Group()
        self.enemy_ships = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.running = True
        self.last_fire_time = 0
        self.fire_cooldown = 100  # Decreased cooldown period in milliseconds
        self.fire_count1 = 0  # Count for ship1 fires
        self.fire_count2 = 0  # Count for ship2 fires
        self.ship1_deaths = 0  # Count for ship1 deaths
        self.ship2_deaths = 0  # Count for ship2 deaths

        # Create enemy ships
        for _ in range(3):  # Add 3 enemy ships
            enemy_ship = EnemyShip(self)
            self.enemy_ships.add(enemy_ship)

        # Initialize user controls
        self.arduino_user = ArduinoUser(self.ship1, self)
        self.pc_user = PCUser(self.ship2, self)

    def run_game(self):
        """Start the main loop for the game."""
        self.arduino_user.start()
        show_start_screen = True
        while self.running:
            if show_start_screen:
                self.start_screen.show()
                show_start_screen = False
            else:
                self._check_events()
                self.arduino_user.update()
                self.pc_user.update()
                self.ship1.update()
                self.ship2.update()
                self._update_bullets()
                self._update_enemy_ships()
                self._update_enemy_bullets()
                self._check_collisions()
                self._update_screen()
                self._debug_ship_position()
                self.clock.tick(60)
        self.arduino_user.join()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._end_game()
                self.pc_user.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.pc_user.check_keyup_events(event)

    def _fire_bullet(self, ship):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self, ship)
        self.bullets.add(new_bullet)
        if ship == self.ship1:
            self.fire_count1 += 1
        elif ship == self.ship2:
            self.fire_count2 += 1

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
        if pygame.sprite.spritecollideany(self.ship1, self.enemy_bullets):
            self.ship1_deaths += 1
            self._reset_game()
        if pygame.sprite.spritecollideany(self.ship2, self.enemy_bullets):
            self.ship2_deaths += 1
            self._reset_game()

    def _reset_game(self):
        """Reset the game state."""
        self.ship1.center_ship()  # Center the first ship
        self.ship2.center_ship()  # Center the second ship
        self.bullets.empty()  # Clear all bullets
        self.enemy_bullets.empty()  # Clear all enemy bullets
        self.enemy_ships.empty()  # Clear all enemy ships

        # Reset the firing state and joystick data
        self.last_fire_time = 0
        self.arduino_user.reset()
        self.pc_user.reset()

        # Create enemy ships
        for _ in range(3):  # Add 3 enemy ships
            enemy_ship = EnemyShip(self)
            self.enemy_ships.add(enemy_ship)

        # Display fire counts
        print(f"Ship1 fired: {self.fire_count1} times")
        print(f"Ship2 fired: {self.fire_count2} times")
        print(f"Ship1 deaths: {self.ship1_deaths}")
        print(f"Ship2 deaths: {self.ship2_deaths}")

    def _end_game(self):
        """Handle ending the game and showing the final results."""
        self.running = False
        print("Game Over!")
        print(f"Ship1 fired: {self.fire_count1} times")
        print(f"Ship2 fired: {self.fire_count2} times")
        print(f"Ship1 deaths: {self.ship1_deaths}")
        print(f"Ship2 deaths: {self.ship2_deaths}")

        # Pass the results to the start screen
        results = {
            'fire_count1': self.fire_count1,
            'fire_count2': self.fire_count2,
            'ship1_deaths': self.ship1_deaths,
            'ship2_deaths': self.ship2_deaths
        }
        self.start_screen.show(results)
        self.reset()

    def reset(self):
        """Reset the game state for a new game."""
        self.ship1.center_ship()  # Center the first ship
        self.ship2.center_ship()  # Center the second ship
        self.bullets.empty()  # Clear all bullets
        self.enemy_bullets.empty()  # Clear all enemy bullets
        self.enemy_ships.empty()  # Clear all enemy ships

        # Reset the firing state and joystick data
        self.last_fire_time = 0
        self.fire_count1 = 0
        self.fire_count2 = 0
        self.ship1_deaths = 0
        self.ship2_deaths = 0
        self.arduino_user.reset()
        self.pc_user.reset()

        # Create enemy ships
        for _ in range(3):  # Add 3 enemy ships
            enemy_ship = EnemyShip(self)
            self.enemy_ships.add(enemy_ship)

        self.running = True  # Restart the game loop

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.enemy_bullets.sprites():
            bullet.draw_bullet()
        self.ship1.blitme()
        self.ship2.blitme()
        for enemy_ship in self.enemy_ships.sprites():
            enemy_ship.blitme()
        pygame.display.flip()

    def _debug_ship_position(self):
        """Print the ship's position and movement flags for debugging."""
        print(f"Ship1 position: x={self.ship1.x}, y={self.ship1.y}")
        print(f"Ship2 position: x={self.ship2.x}, y={self.ship2.y}")

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
