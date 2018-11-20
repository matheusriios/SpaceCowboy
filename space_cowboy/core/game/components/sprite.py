__all__ = ('SpriteComponent')


from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame.surface import Surface


class SpriteComponent(Sprite):

    def __init__(self, position: Vector2, image: Surface):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

    @property
    def position(self):

        return Vector2(self.rect.center)

    @position.setter
    def position(self, value: Vector2):

        self.rect.center = value
