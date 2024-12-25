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
        self.selected_setting = None
        self.settings_list = list(self.settings_manager.scroll_bars.keys())
        self.enter_pressed = False

    def show(self, results=None):
        """Display the start screen."""
        self.screen.fill(self.settings.bg_color)
        self._draw_text("Welcome to Alien Invasion", 48, self.screen_rect.centerx, self.screen_rect.centery - 200)
        self._draw_text("Press 'Enter' to start", 24, self.screen_rect.centerx, self.screen_rect.centery - 170)
        self._draw_text("Press 'ESC' to exit", 24, self.screen_rect.centerx, self.screen_rect.centery - 140)

        self._draw_text("Customizable Settings", 24, self.screen_rect.centerx, self.screen_rect.centery - 110)
        self._draw_text("Ship Speed:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery - 80)
        self._draw_text("Bullet Speed:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery - 50)
        self._draw_text("Enemy Speed:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery - 20)
        self._draw_text("Enemy Bullet Speed:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery + 10)
        self._draw_text("Difficulty Level:", 24, self.screen_rect.centerx - 200, self.screen_rect.centery + 40)

        # Draw scroll bars for customizable settings
        self.settings_manager.draw_scroll_bars(self.screen)

        # Highlight the selected setting
        if self.selected_setting is not None:
            selected_bar = self.settings_manager.scroll_bars[self.selected_setting]
            pygame.draw.rect(self.screen, (255, 0, 0), selected_bar['rect'], 2)  # Red border for the selected setting

        # Display results if provided
        if results:
            self._draw_text(f"Ship1 fired: {results['fire_count1']} times", 24, self.screen_rect.centerx, self.screen_rect.centery + 80)
            self._draw_text(f"Ship2 fired: {results['fire_count2']} times", 24, self.screen_rect.centerx, self.screen_rect.centery + 110)
            self._draw_text(f"Ship1 deaths: {results['ship1_deaths']}", 24, self.screen_rect.centerx, self.screen_rect.centery + 140)
            self._draw_text(f"Ship2 deaths: {results['ship2_deaths']}", 24, self.screen_rect.centerx, self.screen_rect.centery + 170)

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
                        self.enter_pressed = True
                        waiting = False
                    elif event.key == pygame.K_UP:
                        self._select_previous_setting()
                    elif event.key == pygame.K_DOWN:
                        self._select_next_setting()
                    elif event.key == pygame.K_LEFT:
                        self._decrease_selected_setting()
                    elif event.key == pygame.K_RIGHT:
                        self._increase_selected_setting()
                self.settings_manager.handle_event(event)
                self._update_screen()

    def _select_previous_setting(self):
        """Select the previous setting in the list."""
        if self.selected_setting is None:
            self.selected_setting = self.settings_list[-1]
        else:
            index = self.settings_list.index(self.selected_setting)
            self.selected_setting = self.settings_list[index - 1]

    def _select_next_setting(self):
        """Select the next setting in the list."""
        if self.selected_setting is None:
            self.selected_setting = self.settings_list[0]
        else:
            index = self.settings_list.index(self.selected_setting)
            self.selected_setting = self.settings_list[(index + 1) % len(self.settings_list)]

    def _decrease_selected_setting(self):
        """Decrease the value of the selected setting."""
        if self.selected_setting is not None:
            bar = self.settings_manager.scroll_bars[self.selected_setting]
            bar['value'] = max(bar['min_val'], bar['value'] - 0.1)
            bar['slider_rect'].x = bar['rect'].x + (bar['value'] - bar['min_val']) / (bar['max_val'] - bar['min_val']) * bar['rect'].width

    def _increase_selected_setting(self):
        """Increase the value of the selected setting."""
        if self.selected_setting is not None:
            bar = self.settings_manager.scroll_bars[self.selected_setting]
            bar['value'] = min(bar['max_val'], bar['value'] + 0.1)
            bar['slider_rect'].x = bar['rect'].x + (bar['value'] - bar['min_val']) / (bar['max_val'] - bar['min_val']) * bar['rect'].width

    def _update_screen(self):
        """Update the start screen."""
        self.show()
