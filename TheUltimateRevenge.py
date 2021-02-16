import pygame as pg
import settings as st

# start the pygame
pg.init()
WIN = pg.display.set_mode((st.WIN_WIDTH, st.WIN_HEIGHT))
pg.display.set_caption('The Ultimate Revenge!')

HERO_IMG = pg.image.load(st.HERO_IMG_PATH)
HERO = pg.transform.scale(HERO_IMG, (55, 40))


def draw_window():
    """This one is for drawing the gameplay window"""

    WIN.fill((255, 255, 255))
    WIN.blit(HERO, (400, 400))
    pg.display.update()


def main():
    """Main function for running the game"""

    clock = pg.time.Clock()
    run = True
    while run:
        clock.tick(st.FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        draw_window()

    pg.quit()


if __name__ == "__main__":
    main()