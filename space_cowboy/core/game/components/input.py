__all__ = (
    'PlayerInputComponent'
)


from typing import Any

from pygame.event import EventType
from pygame.locals import (
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_UP,
    KEYDOWN,
    KEYUP,
)
from pygame.math import Vector2

from ...systems.events import EventSystem


class PlayerInputComponent:

    def __init__(self, event_system: EventSystem):

        event_system.subscribe(self, self.event_dispatcher, (KEYDOWN, KEYUP))
        self.__direction_vec = Vector2(0, 0)

    def update(self, entity):

        entity.move(self.__direction_vec)

    def event_dispatcher(self, event: EventType):

        if event.key in (K_DOWN, K_LEFT, K_RIGHT, K_UP):
            self.process_movement(event)

    def process_movement(self, event: EventType):

        if event.key == K_DOWN:
            if event.type == KEYDOWN:
                self.__direction_vec.y += 1
            elif event.type == KEYUP:
                self.__direction_vec.y -= 1
        elif event.key == K_LEFT:
            if event.type == KEYDOWN:
                self.__direction_vec.x -= 1
            elif event.type == KEYUP:
                self.__direction_vec.x += 1
        elif event.key == K_RIGHT:
            if event.type == KEYDOWN:
                self.__direction_vec.x += 1
            elif event.type == KEYUP:
                self.__direction_vec.x -= 1
        elif event.key == K_UP:
            if event.type == KEYDOWN:
                self.__direction_vec.y -= 1
            elif event.type == KEYUP:
                self.__direction_vec.y += 1
