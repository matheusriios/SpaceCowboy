__all__ = ('start',)


from pygame.locals import QUIT
from pygame.surface import Surface

from .game.controllers import GameController
from .handlers.initialization import (
    init_clock,
    init_pygame,
    init_screen,
    quit_pygame
)
from .systems import EventSystem


def _configure_screen(configs: dict) -> Surface:

    title = f"{configs['title']} - Version {configs['version']}"
    screen_conf = configs['screen']
    screen = init_screen(title, screen_conf['size'], screen_conf['depth'], screen_conf['is_fullscreen'],
                         screen_conf['is_mouse_visible'])
    return screen


def start(configs: dict):

    init_pygame()
    screen = _configure_screen(configs)
    clock = init_clock()

    event_system = EventSystem()
    event_system.subscribe(__name__, lambda event: quit_pygame(), QUIT)

    game_controller = GameController(event_system)

    while True:

        game_controller.process_events()
        game_controller.update()
        clock.tick(60)
