__all__ = (
    'Asteroid',
    'Ship',
)


from typing import Iterable
from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame.surface import Surface


class Asteroid(Sprite):

    def __init__(self, position: Iterable, direction: Iterable, speed: float, image: Surface):

        super().__init__()
        self.__direction = Vector2(direction)
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position


    @property
    def direction(self) -> Vector2:

        return self.__direction


    @direction.setter
    def direction(self, value: Iterable) -> None:

        self.__direction = Vector2(value)


    @property
    def position(self) -> Vector2:

        return Vector2(self.rect.x, self.rect.y)


    def update(self) -> None:

        vec = self.direction * self.speed
        self.rect.move_ip(vec)


class Ship(Sprite):

    def __init__(self, position: Iterable, direction: Iterable, speed: float, image: Surface):

        super().__init__()
        self.__direction = Vector2(direction)
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position


    @property
    def direction(self) -> Vector2:

        return self.__direction


    @direction.setter
    def direction(self, value: Iterable) -> None:

        self.__direction = Vector2(value)


    @property
    def position(self) -> Vector2:

        return Vector2(self.rect.center)


    def update(self):

        vec = self.direction * self.speed
        self.rect.move_ip(vec)
