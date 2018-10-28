__all__ = (
    'VERSION',
    'GAME_PATH',
    'ASSETS_PATH',
    'ASSETS_BACKGROUNDS_PATH',
    'ASSETS_SOUNDS_PATH',
    'ASSETS_SPRITES_PATH',
    'SCREEN_DEPTH',
    'SCREEN_FULLSCREEN',
    'SCREEN_SIZE',
)


from os import path


VERSION = "0.0.1"
GAME_PATH = path.dirname(path.abspath(__file__))

ASSETS_PATH = path.join(GAME_PATH, 'assets')
ASSETS_BACKGROUNDS_PATH = path.join(ASSETS_PATH, 'backgrounds')
ASSETS_SOUNDS_PATH = path.join(ASSETS_PATH, 'sounds')
ASSETS_SPRITES_PATH = path.join(ASSETS_PATH, 'sprites')

SCREEN_DEPTH = 32
SCREEN_FULLSCREEN = True
SCREEN_SIZE = (1024, 768)
