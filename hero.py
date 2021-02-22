import pygame
from settings import HERO_IMG_PATH, get_img_path


class Hero:
    """Define hero object"""

    def __init__(self, screen, coords):
        self._color = (0, 0, 0)
        self.screen = screen
        self._hero_img = pygame.image.load(HERO_IMG_PATH)
        # self._hero_img = pygame.transform.scale(self._hero_img_raw, (100, 100))
        self._speed = self._width = self._height = 64
        self._flat_y, self._flat_x, self._start_x, self._start_y = coords
        self._rect = pygame.draw.rect(screen, self._color, (self._start_x, self._start_y, self._width, self._height))
        self._all_hero_tiles = self._load_hero_tiles()

    def _load_hero_tiles(self):
        """Read images to animate walking hero"""

        all_hero_tiles = {}
        directions = ['left', 'right', 'top', 'bottom']
        total_tiles = 4
        for direction in directions:
            hero_tiles = []
            for tile_idx in range(total_tiles):
                hero_tiles.append(pygame.image.load(get_img_path('hero_walking\\{}\\tile00{}.png'.format(direction,
                                                                                                         tile_idx))))
            all_hero_tiles[direction] = hero_tiles
        return all_hero_tiles

    def handle_keys(self, level):
        """Handle actions from keyboard"""

        def move_left():
            self._rect.move_ip(-self._speed, 0)
            self._flat_x -= 1

        def move_right():
            self._rect.move_ip(self._speed, 0)
            self._flat_x += 1

        def move_top():
            self._rect.move_ip(0, -self._speed)
            self._flat_y -= 1

        def move_bottom():
            self._rect.move_ip(0, self._speed)
            self._flat_y += 1

        allowed_fields = [' ', 'h']
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and level[self._flat_y][self._flat_x - 1] in allowed_fields:
            move_left()
        elif key[pygame.K_RIGHT] and level[self._flat_y][self._flat_x + 1] in allowed_fields:
            move_right()
        elif key[pygame.K_UP] and level[self._flat_y - 1][self._flat_x] in allowed_fields:
            move_top()
        elif key[pygame.K_DOWN] and level[self._flat_y + 1][self._flat_x] in allowed_fields:
            move_bottom()
        
    def _check_collision(self, field):
        """Check if there is an non-empty field on the way"""
        return field is not None

    def draw(self, screen):
        """Draw hero on screen"""
        self.screen.blit(self._hero_img, self._rect)
