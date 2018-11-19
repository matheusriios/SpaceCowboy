__all__ = (
    'init_pygame',
    'init_screen',
    'quit_pygame',
)


import sys

import pygame
from pygame.surface import Surface
from pygame.time import Clock

from ..typedefs import ScreenSize


def init_clock() -> Clock:

    return Clock()


def init_pygame():

    # TODO Negative values for Linux PulseAudio. Verify if Windows support negative values.
    # FIXME If there is another application using PulseAudio, the program can't start.
    pygame.mixer.pre_init(44100, -16, 2, 1024*4)
    pygame.init()


def init_screen(caption: str, size: ScreenSize, depth: int, is_fullscreen: bool, is_mouse_visible: bool) -> Surface:

    screen = pygame.display.set_mode(size, is_fullscreen, depth)
    pygame.display.set_caption(caption)
    pygame.mouse.set_visible(is_mouse_visible)
    return screen


def quit_pygame():

    pygame.quit()
    sys.exit()
