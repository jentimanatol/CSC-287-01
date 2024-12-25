import pygame

class PCUser:
    """Class to handle PC keyboard input."""

    def __init__(self, ship, game):
        """Initialize the PC user."""
        self.ship = ship
        self.game = game

    def check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.game._fire_bullet(self.ship)

    def check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def update(self):
        """Update ship's position based on keyboard input."""
        pass  # No need to update in this class, as pygame events handle this



    def reset(self):
        """Reset keyboard data to initial state."""
        self.ship.moving_right = False
        self.ship.moving_left = False
        self.ship.moving_up = False
        self.ship.moving_down = False
        print("PC user controls reset to initial state.")




        '''
    def reset(self):
        """Reset keyboard data to initial state."""
        pass  # No need to reset in this class, as there is no persistent state
        '''