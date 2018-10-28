__all__ = (
    'ASSETS_PATH',
    'ASSETS_BACKGROUNDS_PATH',
    'ASSETS_SFX_PATH',
    'ASSETS_SPRITES_PATH',
    'GAME_PATH',
)


from os import path


GAME_PATH = path.dirname(path.abspath(__file__))


ASSETS_PATH = path.join(GAME_PATH, 'assets')
ASSETS_BACKGROUNDS_PATH = path.join(ASSETS_PATH, 'backgrounds')
ASSETS_SFX_PATH = path.join(ASSETS_PATH, 'sfx')
ASSETS_SPRITES_PATH = path.join(ASSETS_PATH, 'sprites')
