import pygame
import settings as st
from hero import Hero
from platform import Platform

pygame.init()
WIN = pygame.display.set_mode((st.WIN_WIDTH, st.WIN_HEIGHT))
pygame.display.set_caption('The Ultimate Revenge!')

hero = Hero(WIN)
platform  = Platform(WIN)


def draw_window():
    """This one is for drawing the gameplay window"""

    WIN.fill((255, 255, 255))
    hero.draw(WIN)
    platform.draw(WIN)
    hero.handle_keys()
    hero.check_bottom_collision(platform.get_rect())
    pygame.display.update()


def main():
    """Main function for running the game"""

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(st.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
