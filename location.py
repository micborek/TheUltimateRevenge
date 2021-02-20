import pygame
from settings import WIN_WIDTH, WIN_HEIGHT

class Location:
    def __init__(self, map):
        self._map = map
        self._color = (255, 0, 0)
        self._width = self._height = 20
        self._map_height = len(self._map) * self._height
        self._map_width = len(self._map[0]) * self._width
        self._start_y = (WIN_HEIGHT - self._map_height) / 2
        self._start_x = (WIN_WIDTH - self._map_width) / 2
        self._fields = {}
    
    def get_starting_hero_cords(self):
        """Calculate starting hero coordinates"""
        for row_idx, row in enumerate(self._map):
            for cell_idx, cell in enumerate(row):
                if cell == 'h':
                    return row_idx, cell_idx, self._start_x + cell_idx * self._width, self._start_y + row_idx * self._height

    def draw(self, screen):
        """Draw location"""
        for row_idx, row in enumerate(self._map):
            fields_row = {}
            for cell_idx, cell in enumerate(row):
                if cell == 'x':
                    fields_row[cell_idx] = pygame.draw.rect(screen, self._color, (self._start_x + cell_idx * self._width, self._start_y + row_idx * self._height, self._width, self._height))
                    fields_row[cell_idx]
            self._fields[row_idx] = fields_row

    def get_fields(self):
        return self._fields
