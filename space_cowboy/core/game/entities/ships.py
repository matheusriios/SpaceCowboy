__all__ = ('PlayerShip',)


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
from pygame.sprite import Sprite

from ..components.input import KeyboardInputComponent
from ..components.sprite import SpriteComponent


class PlayerShip(Sprite):

    def __init__(self, direction: Vector2, velocity: int, sprite_component: SpriteComponent,
                 input_component: KeyboardInputComponent):

        super().__init__()

        self.__direction = direction
        self.__velocity = velocity

        self.__components = {
            'input_component': self.__init_input_component(input_component),
            'sprite_component': sprite_component
        }

    @property
    def image(self):

        return self.__components['sprite_component'].image

    @property
    def rect(self):

        return self.__components['sprite_component'].rect

    def __init_input_component(self, component: KeyboardInputComponent):

        mapping = {
            key: {action: self.__move
                  for action in (KEYDOWN, KEYUP)}
            for key in (K_DOWN, K_LEFT, K_RIGHT, K_UP)
        }
        return component.update_keys(mapping)

    def __move(self, event):

        if event.key == K_DOWN:
            if event.type == KEYDOWN:
                self.__direction.y += 1
            elif event.type == KEYUP:
                self.__direction.y -= 1
        elif event.key == K_LEFT:
            if event.type == KEYDOWN:
                self.__direction.x -= 1
            elif event.type == KEYUP:
                self.__direction.x += 1
        elif event.key == K_RIGHT:
            if event.type == KEYDOWN:
                self.__direction.x += 1
            elif event.type == KEYUP:
                self.__direction.x -= 1
        elif event.key == K_UP:
            if event.type == KEYDOWN:
                self.__direction.y -= 1
            elif event.type == KEYUP:
                self.__direction.y += 1

    def destroy(self):

        for component in self.__components.values():
            component.destroy()
            del component

    def update(self, *args):

        self.__components['sprite_component'].position += self.__direction * self.__velocity
        for component in self.__components.values():
            component.update()
