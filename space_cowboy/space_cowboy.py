__all__ = (
    'main',
)


import os
import pygame
from pygame.locals import (
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_UP,
    KEYDOWN,
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
from consts import (
    ASSETS_SOUNDS_PATH,
    ASSETS_SPRITES_PATH,
)
from typedefs import (
    Colorkey,
    Event
)


def load_image(path: str) -> Surface:

    file_path = os.path.join(ASSETS_SPRITES_PATH, path)
    return pygame.image.load(file_path)


def load_image_surface(path: str, colorkey: Colorkey = None) -> Surface:

    image = load_image(path).convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


def load_image_surface_alpha(path: str) -> Surface:

    image = load_image(path).convert_alpha()
    return image


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

    test_image1 = load_image_surface_alpha(os.path.join('tests', 'test1.png'))
    test_image2 = load_image_surface_alpha(os.path.join('tests', 'test2.png'))
    test_image2_rect = test_image2.get_rect()
    test_sound_ogg = load_sound(os.path.join('tests', 'test1.ogg'))
    test_sound_wav = load_sound(os.path.join('tests', 'test1.wav'))

    screen.blit(background, (0, 0))
    screen.blit(test_image2, (0, 10))
    screen.blit(test_image1, (0, 0))
    pygame.display.flip()

    while True:
        event: Event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == MOUSEBUTTONDOWN:
                button = event.button
                if button == 1:
                    test_sound_ogg.play()
                elif button == 3:
                    test_sound_wav.play()
            elif event.type == KEYDOWN:
                key = event.key
                if key == K_DOWN:
                    test_image2_rect = test_image2_rect.move(0, 10)
                elif key == K_LEFT:
                    test_image2_rect = test_image2_rect.move(-10, 0)
                elif key == K_RIGHT:
                    test_image2_rect = test_image2_rect.move(10, 0)
                elif key == K_UP:
                    test_image2_rect = test_image2_rect.move(0, -10)

        screen.blit(background, (0, 0))
        screen.blit(test_image2, test_image2_rect)
        screen.blit(test_image1, pygame.mouse.get_pos())
        pygame.display.flip()


if __name__ == '__main__':
    main()
