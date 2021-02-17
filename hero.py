import pygame


class Hero:
    def __init__(self, screen):
        self._color = (0, 0, 0)
        self._speed = 5
        self._rect = pygame.draw.rect(screen, self._color, (200, 200, 50, 50))
        self._bottom_collison = False
        

    def handle_keys(self):
        """Handle actions from keyboard"""

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self._rect.move_ip(-self._speed, 0)
        if key[pygame.K_RIGHT]:
            self._rect.move_ip(self._speed, 0)
        if key[pygame.K_UP]:
            self._rect.move_ip(0, -self._speed)
        if key[pygame.K_DOWN] and not self._bottom_collison:
            self._rect.move_ip(0, self._speed)

    def draw(self, screen):
        """Draw hero on screen"""

        pygame.draw.rect(screen, self._color, self._rect)

    def check_bottom_collision(self, platform):
        if self._rect.colliderect(platform):
            self._bottom_collison = True
        else:
            self._bottom_collison = False
