import pygame as pg
import settings as st
from hero import Hero

pg.init()
WIN = pg.display.set_mode((st.WIN_WIDTH, st.WIN_HEIGHT))
pg.display.set_caption('The Ultimate Revenge!')

hero = Hero(WIN)

def draw_window():
    """This one is for drawing the gameplay window"""

    WIN.fill((255, 255, 255))
    hero.draw(WIN)
    hero.handle_keys()
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