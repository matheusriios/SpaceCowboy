__all__ = (
    'ASSETS_PATH',
    'ASSETS_BACKGROUNDS_PATH',
    'ASSETS_IMAGES_PATH',
    'ASSETS_SFX_PATH',
    'GAME_PATH',
)


from os import path


GAME_PATH = path.dirname(path.abspath(__file__))

ASSETS_PATH = path.join(GAME_PATH, 'assets')
ASSETS_BACKGROUNDS_PATH = path.join(ASSETS_PATH, 'backgrounds')
ASSETS_IMAGES_PATH = path.join(ASSETS_PATH, 'images')
ASSETS_SFX_PATH = path.join(ASSETS_PATH, 'sfx')
