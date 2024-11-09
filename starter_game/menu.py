import pygame
import sys
from settings import Settings
from bird import Bird
from plant import Plant
from sound import Sound

class Menu:
    """A class to manage the game menu."""

    def __init__(self, game):
        """Initialize the menu."""
        self.screen = game.screen
        self.settings = game.settings
        self.font = pygame.font.SysFont(None, 48)

    def show_menu(self):
        """Display the menu."""
        self.screen.fill(self.settings.bg_color)
        title = self.font.render("Bird/Plant Game", True, (0, 0, 0))
        play_button = self.font.render("Press Enter to Play", True, (0, 0, 0))

        title_rect = title.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 3))
        play_button_rect = play_button.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2))

        self.screen.blit(title, title_rect)
        self.screen.blit(play_button, play_button_rect)
        pygame.display.flip()

    def wait_for_input(self):
        """Wait for the player to press Enter to start the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return

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
        self.sound = Sound()
        self.menu = Menu(self)

        # Set a timer event for updating the plant image every second
        self.PLANT_UPDATE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.PLANT_UPDATE_EVENT, 1000)

    def run_game(self):
        """Start the main loop for the game."""
        self.menu.show_menu()
        self.menu.wait_for_input()
        while True:
            self._check_events()
            self.bird.update()
            self._check_collisions()
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

    def _check_collisions(self):
        """Check for collisions between the bird and the plant."""
        if pygame.sprite.collide_rect(self.bird, self.plant):
            self.sound.play_explosion()
            self.settings.collisions += 1
            self.bird.reset_position()

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
