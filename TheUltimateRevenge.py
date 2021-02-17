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
    """Draw the game-play window"""

    background_img = pygame.image.load(st.BACKGROUND_IMG_PATH)
    background = pygame.transform.scale(background_img, (1024, 500))

    floor_img = pygame.image.load(st.FLOOR_IMG_PATH)
    floor = pygame.transform.scale(floor_img, (1024, 500))

    WIN.fill((255, 255, 255))
    WIN.blit(floor, (0, 500))
    WIN.blit(background, (0, 0))
    hero.draw(WIN)
    platform.draw(WIN)
    hero.handle_keys()
    hero.check_bottom_collision(platform.get_rect())
    pygame.display.update()


def main():
    """Run the game"""

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
