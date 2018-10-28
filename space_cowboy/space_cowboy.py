__all__ = (
    'main',
)


import os
import pygame
from pygame.event import Event
from pygame.locals import (
    MOUSEBUTTONDOWN,
    RLEACCEL,
    QUIT,
)
from pygame.mixer import Sound
from pygame.sprite import (
    Group,
    Sprite,
)
from pygame.surface import Surface
from pygame.time import Clock
from pygame.transform import smoothscale
from consts import (
    ASSETS_BACKGROUNDS_PATH,
    ASSETS_SOUNDS_PATH,
    ASSETS_SPRITES_PATH,
)
from typedefs import (
    Colorkey,
    ScreenSize,
    Vector2,
)


class Asteroid(Sprite):

    def __init__(self, position: Vector2, direction: Vector2, speed: float, image: Surface):

        super().__init__()
        self.direction = direction
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position


    def update(self):

        position = self.position[0] + self.direction[0] * self.speed, self.position[1] + self.direction[1] * self.speed
        self.rect.x, self.rect.y = position


    @property
    def position(self) -> Vector2:

        return self.rect.x, self.rect.y


class GameController:

    def __init__(self, display: Surface):

        self.__state = 'running'
        self.__background = smoothscale(load_image_surface(os.path.join(ASSETS_BACKGROUNDS_PATH, 'stars_blue.png')),
                                        (1024, 768))
        self.__sprites_list = Group()

        for i in range(0, 10):
            position = ((i + 1) * 80, 0)
            direction = (0, 1)
            speed = 2
            path = os.path.join(ASSETS_SPRITES_PATH, 'asteroids', 'meteor_brown_big1.png')
            img = load_image_surface_alpha(path)
            asteroid = Asteroid(position, direction, speed, img)
            self.__sprites_list.add(asteroid)

        display.blit(self.__background, (0, 0))


    def process_events(self) -> bool:

        event: Event
        for event in pygame.event.get():
            if event.type == QUIT:
                return True

        return False


    def process_updates(self):

        self.__sprites_list.update()


    def display_frame(self, display: Surface):

        self.__sprites_list.clear(display, self.__background)
        self.__sprites_list.draw(display)
        pygame.display.flip()


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

    # TODO Negative values for Linux PulseAudio. Verify if Windows support negative values.
    # TODO If there is another application using PulseAudio, the program can't start.  
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
    clock = Clock()

    game_controller = GameController(screen)

    while True:

        done = game_controller.process_events()
        if done:
            quit_pygame()

        game_controller.process_updates()
        game_controller.display_frame(screen)
        clock.tick(60)


if __name__ == '__main__':
    main()
