#sound.py 
# audio file directory . assets\sounds\explosion.flac
import pygame

class Sound:
    """A class to manage game sounds."""

    def __init__(self):
        """Initialize the game's sound effects."""
        pygame.mixer.init()
        self.explosion_sound = pygame.mixer.Sound('C:\\BHCC\\python\\CSC-287-01\\starter_game\\assets\\sounds\\explosion.flac')

    def play_explosion(self):
        """Play the explosion sound."""
        self.explosion_sound.play()
