import pygame
from pygame.locals import *

class SettingsManager:
    def __init__(self, settings):
        self.settings = settings
        self.font = pygame.font.SysFont(None, 24)
        self.scroll_bars = self._create_scroll_bars()

    def _create_scroll_bars(self):
        """Create scroll bars for custom settings with reasonable limits."""
        scroll_bars = {
            'ship_speed': self._create_scroll_bar(700, 310, self.settings.ship_speed, 0.5, 5.0),
            'bullet_speed': self._create_scroll_bar(700, 340, self.settings.bullet_speed, 1.0, 10.0),
            'bullet_width': self._create_scroll_bar(700, 370, self.settings.bullet_width, 1, 10),
            'bullet_height': self._create_scroll_bar(700, 400, self.settings.bullet_height, 10, 50),
            'enemy_speed': self._create_scroll_bar(700, 430, self.settings.enemy_speed, 0.5, 5.0),
            'enemy_bullet_speed': self._create_scroll_bar(700, 460, self.settings.enemy_bullet_speed, 1.0, 10.0),
            'enemy_bullet_interval': self._create_scroll_bar(700, 490, self.settings.enemy_bullet_interval, 500, 5000)
        }
        return scroll_bars

    def _create_scroll_bar(self, x, y, value, min_val, max_val):
        """Create a scroll bar with default value and limits."""
        rect = pygame.Rect(x, y, 140, 32)
        color = pygame.Color('lightskyblue3')
        slider_rect = pygame.Rect(x + (value - min_val) / (max_val - min_val) * 140, y, 10, 32)
        return {'rect': rect, 'color': color, 'value': value, 'min_val': min_val, 'max_val': max_val, 'slider_rect': slider_rect, 'active': False}

    def draw_scroll_bars(self, screen):
        """Draw scroll bars on the screen."""
        for key, bar in self.scroll_bars.items():
            pygame.draw.rect(screen, bar['color'], bar['rect'], 2)
            pygame.draw.rect(screen, (0, 0, 0), bar['slider_rect'])
            value_surface = self.font.render(str(bar['value']), True, (0, 0, 0))
            screen.blit(value_surface, (bar['rect'].x + bar['rect'].width + 10, bar['rect'].y + 5))

    def handle_event(self, event):
        """Handle events for scroll bars."""
        if event.type == MOUSEBUTTONDOWN:
            for key, bar in self.scroll_bars.items():
                if bar['rect'].collidepoint(event.pos):
                    bar['active'] = True
        if event.type == MOUSEBUTTONUP:
            for key, bar in self.scroll_bars.items():
                bar['active'] = False
        if event.type == MOUSEMOTION:
            for key, bar in self.scroll_bars.items():
                if bar['active']:
                    bar['slider_rect'].x = min(max(event.pos[0], bar['rect'].x), bar['rect'].x + bar['rect'].width - bar['slider_rect'].width)
                    bar['value'] = round(bar['min_val'] + (bar['max_val'] - bar['min_val']) * ((bar['slider_rect'].x - bar['rect'].x) / bar['rect'].width), 2)

    def apply_settings(self):
        """Apply the customized settings."""
        self.settings.ship_speed = self.scroll_bars['ship_speed']['value']
        self.settings.bullet_speed = self.scroll_bars['bullet_speed']['value']
        self.settings.bullet_width = self.scroll_bars['bullet_width']['value']
        self.settings.bullet_height = self.scroll_bars['bullet_height']['value']
        self.settings.enemy_speed = self.scroll_bars['enemy_speed']['value']
        self.settings.enemy_bullet_speed = self.scroll_bars['enemy_bullet_speed']['value']
        self.settings.enemy_bullet_interval = self.scroll_bars['enemy_bullet_interval']['value']
