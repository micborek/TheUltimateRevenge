import pygame
from settings import WIN_WIDTH, WIN_HEIGHT, FENCE_IMG_PATH


class Location:
    def __init__(self, level):
        self._map = level
        self._color = (255, 0, 0)
        self._width = self._height = 64
        self._map_height = len(self._map) * self._height
        self._map_width = len(self._map[0]) * self._width
        self._start_y = (WIN_HEIGHT - self._map_height) / 2
        self._start_x = (WIN_WIDTH - self._map_width) / 2
        self._fields = []
        self._initial_draw()
    
    def get_starting_hero_cords(self):
        """Calculate starting hero coordinates"""
        for row_idx, row in enumerate(self._map):
            for cell_idx, cell in enumerate(row):
                if cell == 'h':
                    return row_idx, cell_idx, self._start_x + cell_idx * self._width, \
                           self._start_y + row_idx * self._height

    def _initial_draw(self):
        for row_idx, row in enumerate(self._map):
            row_fields = []
            for cell_idx, cell in enumerate(row):
                if cell == 'x':
                    fence = pygame.image.load(FENCE_IMG_PATH)
                    fence = pygame.transform.scale(fence, (64, 64))
                    fence_rect = fence.get_rect()
                    fence_rect.x = self._start_x + cell_idx * self._width
                    fence_rect.y = self._start_y + row_idx * self._height
                    row_fields.append((fence, fence_rect))
            self._fields.append(row_fields)

    def draw(self, screen):
        """Draw location"""
        for row in self._fields:
            for img, rect in row:
                screen.blit(img, rect)
