"""Display start screen or menu"""

import pygame
import settings as st


class Logo:
    def __init__(self):
        self.logo_img = pygame.image.load(st.LOGO_IMG_PATH)
        self.logo = pygame.transform.scale(self.logo_img, (1024, 300))


def menu(screen):

    logo = Logo()
    clock = pygame.time.Clock()
    while True:
        clock.tick(st.FPS)
        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if key[pygame.K_SPACE]:
                return

        screen.fill((255, 255, 255))
        screen.blit(logo.logo, (0, 120))
        pygame.display.update()
