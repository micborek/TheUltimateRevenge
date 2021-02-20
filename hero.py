import pygame


class Hero:
    def __init__(self, screen, coords):
        self._color = (0, 0, 0)
        self._speed = self._width = self._height = 20
        self._flat_y, self._flat_x, self._start_x, self._start_y = coords
        self._rect = pygame.draw.rect(screen, self._color, (self._start_x, self._start_y, self._width, self._height))

    def handle_keys(self, map):
        """Handle actions from keyboard"""

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and map[self._flat_y][self._flat_x - 1] == ' ':
            self._rect.move_ip(-self._speed, 0)
            pygame.time.wait(100)
            self._flat_x -= 1
        elif key[pygame.K_RIGHT] and map[self._flat_y][self._flat_x + 1] == ' ':
            self._rect.move_ip(self._speed, 0)
            pygame.time.wait(100)
            self._flat_x += 1
        elif key[pygame.K_UP] and map[self._flat_y - 1][self._flat_x] == ' ':
            self._rect.move_ip(0, -self._speed)
            pygame.time.wait(100)
            self._flat_y -= 1
        elif key[pygame.K_DOWN] and map[self._flat_y + 1][self._flat_x] == ' ':
            self._rect.move_ip(0, self._speed)
            pygame.time.wait(100)
            self._flat_y += 1
        
    def _check_collision(self, field):
        """Check if there is an non-empty field on the way"""
        return field is not None

    def draw(self, screen):
        """Draw hero on screen"""

        pygame.draw.rect(screen, self._color, self._rect)


