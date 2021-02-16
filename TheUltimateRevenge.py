import pygame as pg

# game window resolution
WIN_WIDTH = 1366
WIN_HEIGHT = 768

# start the pygame
pg.init()
pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


def main():
    """Main function for running the game"""

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

    pg.quit()


if __name__ == "__main__":
    main()