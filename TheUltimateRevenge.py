import pygame
import settings as st
from hero import Hero
from level import Floor, Background, Ground
from start_screen import menu
from locations_settings import LOCATION1_MAP
from location import Location

pygame.init()
WIN = pygame.display.set_mode((st.WIN_WIDTH, st.WIN_HEIGHT))
pygame.display.set_caption('The Ultimate Revenge!')

location = Location(LOCATION1_MAP)
hero = Hero(WIN, location.get_starting_hero_cords())


def draw_window():
    """Draw the game-play window"""

    # draw static elements
    WIN.fill((255, 255, 255))
    # handle hero
    hero.draw(WIN)
    location.draw(WIN)
    hero.handle_keys()
    #hero.check_bottom_collision(floor.get_rect())
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
    menu(WIN)
    main()
