import pygame
import sys

class StartScreen:
    """Class to manage the start screen."""

    def __init__(self, ai_game):
        """Initialize the start screen."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

    def show(self):
        """Display the start screen."""
        self.screen.fill(self.settings.bg_color)
        self._draw_text("Welcome to Alien Invasion", 48, self.screen_rect.centerx, self.screen_rect.centery - 50)
        self._draw_text("Press 'Enter' to start", 24, self.screen_rect.centerx, self.screen_rect.centery)
        self._draw_text("Press 'ESC' to exit", 24, self.screen_rect.centerx, self.screen_rect.centery + 30)
        pygame.display.flip()

        # Wait for a key press to start the game
        self._wait_for_key()

    def _draw_text(self, text, size, x, y):
        """Draw text on the screen."""
        font = pygame.font.SysFont(None, size)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def _wait_for_key(self):
        """Wait for a key press to start the game."""
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_RETURN:
                        waiting = False
