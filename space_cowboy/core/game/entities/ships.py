__all__ = ('PlayerShip',)


from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame.surface import Surface

from ..components.input import PlayerInputComponent
from ..components.sprite import SpriteComponent


class PlayerShip(Sprite):

    def __init__(self, direction: Vector2, velocity: int, sprite_component: SpriteComponent,
                 input_component: PlayerInputComponent):

        super().__init__()
        self.__input_component = input_component
        self.__input_component.direction = direction
        self.__direction = direction
        self.__sprite_component = sprite_component
        self.velocity = velocity

    @property
    def image(self):

        return self.__sprite_component.image

    @property
    def rect(self):

        return self.__sprite_component.rect

    @property
    def direction(self) -> Vector2:

        return self.__direction

    @direction.setter
    def direction(self, value: Vector2):

        self.__direction = value

    def update(self):

        self.__input_component.update(self)
        self.__sprite_component.position += self.direction * self.velocity
