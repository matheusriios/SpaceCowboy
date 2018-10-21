__all__ = (
    'main',
)


import os
import pygame
from pygame.locals import (
    K_a,
    K_d,
    K_s,
    K_w,
    K_DOWN,
    K_ESCAPE,
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
    Event,
    ScreenSize,
)


class GameObject:

    def __init__(self, image, position, speed):

        self.image = image
        self.position = image.get_rect().move(*position)
        self.speed = speed

    def move(self, direction):

        vec_x, vec_y = direction
        self.position = self.position.move(vec_x * self.speed, vec_y * self.speed)



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


def quit_pygame():

    pygame.quit()


def init_pygame():

    # TODO:  Negative values for Linux PulseAudio. Verify if Windows support negative values.
    pygame.mixer.pre_init(44100, -16, 2, 1024*4)
    pygame.init()


def init_screen(caption: str, size: ScreenSize, depth: int, is_fullscreen: bool, is_mouse_visible: bool) -> Surface:

    screen = pygame.display.set_mode(size, is_fullscreen, depth)
    pygame.display.set_caption(caption)
    pygame.mouse.set_visible(is_mouse_visible)
    return screen


def main() -> None:

    init_pygame()

    screen = init_screen("Space Cowboy", (1024, 768), 32, True, True)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    text = font.render("Hello, world!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)


    ship_img = load_image_surface_alpha(os.path.join('tests', 'test1.png'))
    asteroid_img = load_image_surface_alpha(os.path.join('tests', 'test2.png'))

    ship = GameObject(ship_img, (100, 100), 10)
    asteroid = GameObject(asteroid_img, (0, 0), 5)

    objects = [ship, asteroid]

    test_sound_ogg = load_sound(os.path.join('tests', 'test1.ogg'))
    test_sound_wav = load_sound(os.path.join('tests', 'test1.wav'))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while True:
        event: Event
        for event in pygame.event.get():
            if event.type == QUIT:
                return quit_pygame()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return quit_pygame()
            if event.type == MOUSEBUTTONDOWN:
                button = event.button
                if button == 1:
                    test_sound_ogg.play()
                elif button == 3:
                    test_sound_wav.play()
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    asteroid.move((-1, 0))
                elif event.key == K_d:
                    asteroid.move((1, 0))
                elif event.key == K_s:
                    asteroid.move((0, 1))
                elif event.key == K_w:
                    asteroid.move((0, -1))
                elif event.key == K_DOWN:
                    ship.move((0, 1))
                elif event.key == K_LEFT:
                    ship.move((-1, 0))
                elif event.key == K_RIGHT:
                    ship.move((1, 0))
                elif event.key == K_UP:
                    ship.move((0, -1))

        screen.blit(background, (0, 0))
        for obj in objects:
            screen.blit(obj.image, obj.position)
        pygame.display.flip()


if __name__ == '__main__':
    main()
