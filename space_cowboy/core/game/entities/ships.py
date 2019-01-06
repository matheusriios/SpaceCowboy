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
from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface

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
    def image(self) -> Surface:

        return self.__components['sprite_component'].image

    @property
    def position(self):

        return self.__components['sprite_component'].position

    @position.setter
    def position(self, value: Vector2):

        self.__components['sprite_component'].position = value

    @property
    def rect(self) -> Rect:

        return self.__components['sprite_component'].rect


    def __init_input_component(self, component: KeyboardInputComponent) -> KeyboardInputComponent:

        mapping = {
            key: {action: self.__change_direction
                  for action in (KEYDOWN, KEYUP)}
            for key in (K_DOWN, K_LEFT, K_RIGHT, K_UP)
        }
        return component.update_keys(mapping)

    def __change_direction(self, event: EventType):

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

        self.position += self.__direction * self.__velocity
        for component in self.__components.values():
            component.update()
