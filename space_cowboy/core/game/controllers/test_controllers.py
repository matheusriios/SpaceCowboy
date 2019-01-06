__all__ = ('GameTestController001')


import os

from pygame.sprite import (
    Group,
    GroupSingle
)
from pygame.surface import Surface

from ...loaders.images import ImagesLoader
from ...systems.events import EventSystem
from ..entities.utils import build_player_ship


class GameTestController001:

    def __init__(self, display: Surface, event_system: EventSystem, images_loader: ImagesLoader):

        self.__display = display
        self.__event_system = event_system

        self.__background = images_loader.smoothscale(
            images_loader.load_surface(
                os.path.join('backgrounds', 'stars_blue.png')),
            self.__display.get_size())
        self.__display.blit(self.__background, (0, 0))

        player = build_player_ship(
            self.__display.get_rect().center, (0, 0), 10, self.__event_system, images_loader)
        self.__player_group = GroupSingle(player)
        self.__sprites_group = Group(player)

    def process_events(self):

        self.__event_system.update()

    def update(self):

        self.__sprites_group.update()
        self.__player_group.sprite.rect.clamp_ip(
            self.__display.get_rect())

    def render_frame(self):

        self.__sprites_group.clear(self.__display, self.__background)
        self.__sprites_group.draw(self.__display)
