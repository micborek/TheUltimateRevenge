import pygame
import settings as st
from hero import Hero
from level import Floor, Background, Ground

pygame.init()
WIN = pygame.display.set_mode((st.WIN_WIDTH, st.WIN_HEIGHT))
pygame.display.set_caption('The Ultimate Revenge!')

hero = Hero(WIN)
floor = Floor(WIN)
background = Background()
ground = Ground()


def draw_window():
    """Draw the game-play window"""

    # draw static elements
    WIN.blit(background.get_background(), (0, 0))
    WIN.blit(ground.get_ground(), (0, 540))

    # handle hero
    hero.draw(WIN)
    hero.handle_keys()
    hero.check_bottom_collision(floor.get_rect())
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
