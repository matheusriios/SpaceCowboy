__all__ = ('GameController',)


import os
import random
from typing import Iterable
from pygame.event import Event
from pygame.locals import (
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_UP,
    KEYDOWN,
    KEYUP,
    QUIT,
)
from pygame.sprite import (
    Group,
    GroupSingle,
    groupcollide,
)
from pygame.surface import Surface
from .objects import (
    Asteroid,
    Ship,
)
from ..loaders.images import ImagesLoader


class GameController:

    def __init__(self, display: Surface, images_loader: ImagesLoader):

        self.__display = display
        self.__images_loader = images_loader

        self.__background = self.__images_loader.smoothscale(
            self.__images_loader.load_surface(
                os.path.join('backgrounds', 'stars_blue.png')),
            self.__display.get_size()
        )
        self.__display.blit(self.__background, (0, 0))

        self.__player = Ship(
            self.__display.get_rect().center,
            (0, 0),
            10,
            self.__images_loader.load_surface_alpha(
                os.path.join('ships', 'ship1_red.png'))
        )

        self.__sprites_list = Group()
        self.__sprites_list.add(self.__player)

        self.__player_group = GroupSingle()
        self.__player_group.add(self.__player)

    def process_events(self, events: Iterable[Event]):

        for event in events:
            if event.type == QUIT:
                return True
            if event.type == KEYDOWN:
                direction = self.__player.direction
                if event.key == K_DOWN:
                    self.__player.direction = (direction[0], 1.0)
                if event.key == K_LEFT:
                    self.__player.direction = (-1.0, direction[1])
                if event.key == K_RIGHT:
                    self.__player.direction = (1.0, direction[1])
                if event.key == K_UP:
                    self.__player.direction = (direction[0], -1.0)
            if event.type == KEYUP:
                direction = self.__player.direction
                if event.key == K_DOWN:
                    self.__player.direction = (direction[0], 0.0)
                if event.key == K_LEFT:
                    self.__player.direction = (0.0, direction[1])
                if event.key == K_RIGHT:
                    self.__player.direction = (0.0, direction[1])
                if event.key == K_UP:
                    self.__player.direction = (direction[0], 0.0)

        return False

    def process_updates(self):

        self.__sprites_list.update()


    def render_frame(self):

        self.__sprites_list.clear(self.__display, self.__background)
        self.__sprites_list.draw(self.__display)
