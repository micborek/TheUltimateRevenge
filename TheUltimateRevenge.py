import pygame
import settings
import sys
from hero import Hero
from start_screen import menu
import locations_maps
from location import Location


def operate():
    """Initialize the application"""

    pygame.init()
    game_window = pygame.display.set_mode((settings.WIN_WIDTH, settings.WIN_HEIGHT))
    pygame.display.set_caption('The Ultimate Revenge!')

    # run the game after the start screen
    if not menu(game_window):
        pygame.quit()
        sys.exit()
    else:
        main(game_window)


def draw_window(game_window, hero, location):
    """Draw the game objects in window"""

    game_window.fill((0, 255, 0))
    hero.draw(game_window)
    location.draw(game_window)
    hero.handle_keys(game_window, locations_maps.LOCATION1_MAP)
    pygame.display.update()


def main(game_window):
    """Run the game"""

    location = Location(locations_maps.LOCATION1_MAP)
    hero = Hero(game_window, location.get_starting_hero_cords())

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(settings.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(game_window, hero, location)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    operate()
