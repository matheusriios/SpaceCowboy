__all__ = ('start',)


from pygame.display import flip
from pygame.event import get as get_events
from pygame.surface import Surface
from .consts import ASSETS_IMAGES_PATH
from .handlers.initialization import (
    init_clock,
    init_pygame,
    init_screen,
    quit_pygame,
)
from .loaders import ImagesLoader
from .game.controllers import GameController


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

    images_loader = ImagesLoader(ASSETS_IMAGES_PATH)
    game_controller = GameController(screen, images_loader)

    while True:

        events = get_events()
        done = game_controller.process_events(events)
        if done:
            quit_pygame()

        game_controller.process_updates()
        game_controller.render_frame()
        flip()
        clock.tick(60)
