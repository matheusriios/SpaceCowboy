__all__ = (
    'main',
)

try:
    import os
    import sys
    import pygame
    from typing import (
        Tuple,
    )
    from pygame.locals import (
        MOUSEBUTTONDOWN,
        QUIT,
        RLEACCEL,
    )
    from pygame.mixer import (
        Sound,
    )
    from pygame.surface import (
        Surface,
    )
    from pygame.rect import (
        Rect,
    )
except ImportError:
    print(f"couldn't load module: {ImportError}")
    sys.exit(2)


# Constants
VERSION = "0.0.1"
GAME_PATH = os.path.dirname(os.path.abspath(__file__))
ASSETS_PATH = os.path.join(GAME_PATH, 'assets')
ASSETS_SOUNDS_PATH = os.path.join(ASSETS_PATH, 'sounds')
ASSETS_SPRITES_PATH = os.path.join(ASSETS_PATH, 'sprites')


# Types
Colorkey = Tuple[int, int, int]


def load_image(path: str) -> Surface:

    file_path = os.path.join(ASSETS_SPRITES_PATH, path)
    return pygame.image.load(file_path)


def load_image_surface(path: str, colorkey: Colorkey = None) -> Tuple[Surface, Rect]:

    image = load_image(path).convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_image_surface_alpha(path: str) -> Tuple[Surface, Rect]:

    image = load_image(path).convert_alpha()
    return image, image.get_rect()


def load_sound(path: str) -> Sound:

    file_path = os.path.join(ASSETS_SOUNDS_PATH, path)
    sound = pygame.mixer.Sound(file_path)
    return sound


def main() -> None:

    # TODO:  Negative values for Linux PulseAudio. Verify if Windows support negative values.
    pygame.mixer.pre_init(44100, -16, 2, 1024*4)
    pygame.init()

    screen = pygame.display.set_mode((1024, 768), True, 32)
    pygame.display.set_caption("Space Cowboy")
    pygame.mouse.set_visible(False)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    text = font.render("Hello, world!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    test_image = load_image(os.path.join('tests', 'test1.png'))
    test_sound_ogg = load_sound(os.path.join('tests', 'test1.ogg'))
    test_sound_wav = load_sound(os.path.join('tests', 'test1.wav'))

    screen.blit(background, (0, 0))
    screen.blit(test_image, (0, 0))
    pygame.display.flip()

    while True:
        event: pygame.event.EventType
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                button = event.button
                if button == 1:
                    test_sound_ogg.play()
                elif button == 3:
                    test_sound_wav.play()
                else:
                    pass

        screen.blit(background, (0, 0))
        screen.blit(test_image, pygame.mouse.get_pos())
        pygame.display.flip()


if __name__ == '__main__':
    main()
