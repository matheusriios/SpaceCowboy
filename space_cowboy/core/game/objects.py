__all__ = ('Asteroid',)


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
        self.rect.x, self.rect.y = position


    @property
    def direction(self) -> Vector2:

        return self.__direction


    @direction.setter
    def direction(self, value: Iterable) -> None:

        self.direction = Vector2(value).normalize_ip()


    @property
    def position(self) -> Vector2:

        return Vector2(self.rect.x, self.rect.y)


    def update(self) -> None:

        vec: Vector2 = self.direction * self.speed
        self.rect.x += vec.x
        self.rect.y += vec.y
