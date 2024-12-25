import pygame
import sys
from setup_settings import SettingsManager

class StartScreen:
    """Class to manage the start screen."""

    def __init__(self, ai_game):
        """Initialize the start screen."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()
        self.settings_manager = SettingsManager(self.settings)

    def show(self, results=None):
        """Display the start screen."""
        self.screen.fill(self.settings.bg_color)
        self._draw_text("Welcome to Alien Invasion", 48, self.screen_rect.centerx, self.screen_rect.centery - 150)
        self._draw_text("Press 'Enter' to start", 24, self.screen_rect.centerx, self.screen_rect.centery - 120)
        self._draw_text("Press 'ESC' to exit", 24, self.screen_rect.centerx, self.screen_rect.centery - 90)

        self._draw_text("Customizable Settings", 24, self.screen_rect.centerx, self.screen_rect.centery - 60)
        self._draw_text("Ship Speed:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery - 90)
        self._draw_text("Bullet Speed:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery - 60)
        self._draw_text("Bullet Width:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery - 30)
        self._draw_text("Bullet Height:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery)
        self._draw_text("Enemy Speed:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery + 30)
        self._draw_text("Enemy Bullet Speed:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery + 60)
        self._draw_text("Enemy Bullet Interval:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery + 90)

        # Draw scroll bars for customizable settings
        self.settings_manager.draw_scroll_bars(self.screen)

        # Display results if provided
        if results:
            self._draw_text(f"Ship1 fired: {results['fire_count1']} times", 24, self.screen_rect.centerx, self.screen_rect.centery + 120)
            self._draw_text(f"Ship2 fired: {results['fire_count2']} times", 24, self.screen_rect.centerx, self.screen_rect.centery + 150)
            self._draw_text(f"Ship1 deaths: {results['ship1_deaths']}", 24, self.screen_rect.centerx, self.screen_rect.centery + 180)
            self._draw_text(f"Ship2 deaths: {results['ship2_deaths']}", 24, self.screen_rect.centerx, self.screen_rect.centery + 210)

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
                        self.settings_manager.apply_settings()
                        waiting = False
                self.settings_manager.handle_event(event)
                self._update_screen()

    def _update_screen(self):
        """Update the start screen."""
        self.show()
