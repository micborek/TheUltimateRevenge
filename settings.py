"""Values for the main game variables"""
import os


def get_img_path(img_file_name):
    """Get path for img file"""
    return os.path.join('source', 'img', img_file_name)


# game window resolution
WIN_WIDTH = 1024
WIN_HEIGHT = 576

# main() loop refresh value
FPS = 60

# img paths
HERO_IMG_PATH = get_img_path('hero.png')
FLOOR_IMG_PATH = get_img_path('floor.png')
BACKGROUND_IMG_PATH = get_img_path('level_background.png')
LOGO_IMG_PATH = get_img_path('logo.png')
