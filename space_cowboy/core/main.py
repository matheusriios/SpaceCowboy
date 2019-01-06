__all__ = ('start',)


from pygame.display import flip
from pygame.locals import QUIT
from pygame.surface import Surface

from .consts import ASSETS_IMAGES_PATH
from .game.controllers import GameTestController001
from .handlers.initialization import (
    init_clock,
    init_pygame,
    init_screen,
    quit_pygame
)
from .loaders.images import ImagesLoader
from .systems import EventSystem


def _configure_screen(configs: dict) -> Surface:

    title = f"{configs['title']} - Version {configs['version']}"
    screen_conf = configs['screen']
    screen = init_screen(title, screen_conf['size'], screen_conf['depth'],
                         screen_conf['is_fullscreen'], screen_conf['is_mouse_visible'])
    return screen


def start(configs: dict):

    init_pygame()
    screen = _configure_screen(configs)
    clock = init_clock()

    event_system = EventSystem()
    event_system.subscribe(__name__, lambda event: quit_pygame(), QUIT)

    images_loader = ImagesLoader(ASSETS_IMAGES_PATH)

    game_controller = GameTestController001(screen, event_system, images_loader)

    while True:

        game_controller.process_events()
        game_controller.update()
        game_controller.render_frame()
        flip()
        clock.tick(60)
