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
from ..components.model import ModelComponent
from ..components.transform import TransformComponent


class PlayerShip(Sprite):

    def __init__(self, ic: KeyboardInputComponent, mc: ModelComponent, tc: TransformComponent):

        super().__init__()
        self.__components = {
            'input_component': self.__init_input_component(ic),
            'model_component': mc,
            'transform_component': tc
        }

    @property
    def image(self) -> Surface:

        return self.__components['model_component'].image

    @property
    def position(self):

        return self.__components['model_component'].position

    @position.setter
    def position(self, value: Vector2):

        self.__components['model_component'].position = value

    @property
    def rect(self) -> Rect:

        return self.__components['model_component'].rect


    def __init_input_component(self, component: KeyboardInputComponent) -> KeyboardInputComponent:

        mapping = {
            key: {action: self.__change_direction
                  for action in (KEYDOWN, KEYUP)}
            for key in (K_DOWN, K_LEFT, K_RIGHT, K_UP)
        }
        return component.update_keys(mapping)

    def __change_direction(self, event: EventType):

        direction = self.__components['transform_component']
        if event.key == K_DOWN:
            if event.type == KEYDOWN:
                direction.y += 1
            elif event.type == KEYUP:
                direction.y -= 1
        elif event.key == K_LEFT:
            if event.type == KEYDOWN:
                direction.x -= 1
            elif event.type == KEYUP:
                direction.x += 1
        elif event.key == K_RIGHT:
            if event.type == KEYDOWN:
                direction.x += 1
            elif event.type == KEYUP:
                direction.x -= 1
        elif event.key == K_UP:
            if event.type == KEYDOWN:
                direction.y -= 1
            elif event.type == KEYUP:
                direction.y += 1

    def destroy(self):

        for component in self.__components.values():
            component.destroy()
            del component

    def update(self, *args):

        self.position += self.__components['transform_component'].velocity
        for component in self.__components.values():
            component.update()
