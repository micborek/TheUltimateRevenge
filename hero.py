import pygame


class Hero:
    def __init__(self, screen, coords):
        self._color = (0, 0, 0)
        self._speed = 30
        self._start_x, self._start_y = coords
        self._rect = pygame.draw.rect(screen, self._color, (self._start_x, self._start_y, 30, 30))
        self._bottom_collision = False

    def handle_keys(self):
        """Handle actions from keyboard"""

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self._rect.move_ip(-self._speed, 0)
            pygame.time.wait(100)
        elif key[pygame.K_RIGHT]:
            self._rect.move_ip(self._speed, 0)
            pygame.time.wait(100)
        elif key[pygame.K_UP]:
            self._rect.move_ip(0, -self._speed)
            pygame.time.wait(100)
        elif key[pygame.K_DOWN] and not self._bottom_collision:
            self._rect.move_ip(0, self._speed)
            pygame.time.wait(100)

    def draw(self, screen):
        """Draw hero on screen"""

        pygame.draw.rect(screen, self._color, self._rect)

    def check_bottom_collision(self, platform):
        if self._rect.colliderect(platform):
            self._bottom_collision = True
        else:
            self._bottom_collision = False
