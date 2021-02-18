import pygame
import settings


class Floor:
    def __init__(self, screen):
        self.height = 20
        self._rect = pygame.draw.rect(screen, (255, 0, 0),
                                      (0, settings.WIN_HEIGHT - self.height, settings.WIN_WIDTH, self.height))

    def draw(self, screen):
        """Draw platform on screen"""
        pygame.draw.rect(screen, (255, 0, 0), self._rect)

    def get_rect(self):
        return self._rect


class Background:
    def __init__(self):
        self.background_img = pygame.image.load(settings.BACKGROUND_IMG_PATH)
        self._background = pygame.transform.scale(self.background_img, (1024, 576))

    def get_background(self):
        return self._background


class Ground:
    def __init__(self):
        self._ground = pygame.image.load(settings.FLOOR_IMG_PATH)

    def get_ground(self):
        return self._ground
