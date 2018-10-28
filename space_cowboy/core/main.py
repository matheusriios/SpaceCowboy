__all__ = ('start',)


from pygame.locals import QUIT
from pygame.surface import Surface
from .engine.handlers.initialization import (
    init_clock,
    init_pygame,
    init_screen,
    quit_pygame,
)


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

    from pygame.event import get as get_events
    while True:

        events = get_events()
        for event in events:
            if event.type == QUIT:
                quit_pygame()
            clock.tick(60)






# def main() -> None:

#     init_pygame()

#     screen = init_screen("Space Cowboy", SCREEN_SIZE, SCREEN_DEPTH, SCREEN_FULLSCREEN, True)
#     clock = Clock()

#     game_controller = GameController(screen)

#     while True:

#         done = game_controller.process_events()
#         if done:
#             quit_pygame()

#         game_controller.process_updates()
#         game_controller.display_frame(screen)
#         pygame.display.flip()
#         clock.tick(60)
