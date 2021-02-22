"""Display start screen or menu"""

import pygame
import settings as st
pygame.font.init()


class Logo:
    def __init__(self):
        self.logo_img = pygame.image.load(st.LOGO_IMG_PATH)
        self.logo = pygame.transform.scale(self.logo_img, (1024, 300))


class StartText:
    def __init__(self, text):
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = my_font.render(text, False, (0, 0, 0))


def menu(screen):
    """Display menu on screen"""

    start_text = StartText('Click any key to start the game!')
    logo = Logo()

    clock = pygame.time.Clock()
    while True:
        clock.tick(st.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                return True

        screen.fill((255, 255, 255))
        screen.blit(logo.logo, (0, 120))
        screen.blit(start_text.text, (250, 450))
        pygame.display.update()
