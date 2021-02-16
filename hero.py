import pygame

class Hero:
    def __init__(self, screen):
        self.rect = pygame.draw.rect(screen, (0, 0, 0), (200, 200, 50, 50))
        self.speed = 2

    def handle_keys(self):
        """Handle actions from keyboard"""
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-self.speed, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(self.speed, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -self.speed)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, self.speed)

    def draw(self, screen):
        """Draw hero on screen"""

        pygame.draw.rect(screen, (0, 0, 0), self.rect)
 