import pygame
import settings

class Platform:
    def __init__(self, screen):
        self.height = 20
        self._rect = pygame.draw.rect(screen, (255, 0, 0), (0, settings.WIN_HEIGHT - self.height, settings.WIN_WIDTH, self.height))

    def draw(self, screen):
        """Draw platform on screen"""

        pygame.draw.rect(screen, (255, 0, 0), self._rect)

    def get_rect(self):
        return self._rect