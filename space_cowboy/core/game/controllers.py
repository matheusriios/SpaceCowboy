__all__ = ('GameController',)


import os

from pygame.sprite import (
    Group,
    GroupSingle,
)
from pygame.surface import Surface

from ..loaders.images import ImagesLoader
from ..systems.events import EventSystem
from .components.input import PlayerInputComponent
from .objects.builders import build_player_ship


class GameController:

    def __init__(self, display: Surface, event_system: EventSystem, images_loader: ImagesLoader):

        self.__display = display
        self.__event_system = event_system
        self.__images_loader = images_loader

        self.__background = self.__images_loader.smoothscale(
            self.__images_loader.load_surface(
                os.path.join('backgrounds', 'stars_blue.png')
            ), self.__display.get_size()
        )
        self.__display.blit(self.__background, (0, 0))

        self.__player_input = PlayerInputComponent(self.__event_system)
        self.__player = build_player_ship(
            self.__display.get_rect().midbottom, (0, 0), 10, self.__images_loader, self.__player_input
        )

        self.__player_group = GroupSingle(self.__player)
        self.__sprites_group = Group(self.__player)

    def process_events(self):

        self.__event_system.update()

    def update(self):

        self.__sprites_group.update()

    def render_frame(self):

        self.__sprites_group.clear(self.__display, self.__background)
        self.__sprites_group.draw(self.__display)
