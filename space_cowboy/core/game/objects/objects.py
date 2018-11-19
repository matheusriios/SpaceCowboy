__all__ = (
    'PlayerShip',
)


from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame.surface import Surface

from ..components.input import PlayerInputComponent


class PlayerShip(Sprite):

    def __init__(self, position: Vector2, direction: Vector2, velocity: int, image: Surface,
                 input_component: PlayerInputComponent):

        super().__init__()
        self.__input_component = input_component
        self.__input_component.direction = direction
        self.__direction = direction
        self.velocity = velocity
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

    @property
    def direction(self) -> Vector2:

        return self.__direction

    @direction.setter
    def direction(self, value: Vector2):

        self.__direction = value

    @property
    def position(self) -> Vector2:

        return Vector2(self.rect.center)

    def update(self):

        self.__input_component.update(self)
        self.rect.center += self.__direction * self.velocity
