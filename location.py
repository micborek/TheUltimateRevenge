import pygame
from settings import WIN_WIDTH, WIN_HEIGHT

class Location:
    def __init__(self, map):
        self._map = map
        self._color = (255, 0, 0)
        self._width = self._height = 30
        self._map_height = len(self._map) * self._height
        self._map_width = len(self._map[0]) * self._width
        self._start_y = self._get_starting_cords(self._map_height, WIN_HEIGHT)
        self._start_x = self._get_starting_cords(self._map_width, WIN_WIDTH)

    def _get_starting_cords(self, map_length, win_length):
        """Calculate starting coordinates for map"""
        return (win_length - map_length)/2
    
    def get_starting_hero_cords(self):
        """Calculate starting hero coordinates"""
        for row_idx, row in enumerate(self._map):
            for cell_idx, cell in enumerate(row):
                if cell == 'h':
                    return self._start_x + cell_idx * self._width, self._start_y + row_idx * self._height

    def draw(self, screen):
        """Draw location"""
        for row_idx, row in enumerate(self._map):
            for cell_idx, cell in enumerate(row):
                if cell == 'x':
                    pygame.draw.rect(screen, self._color, (self._start_x + cell_idx * self._width, self._start_y + row_idx * self._height, self._width, self._height))

