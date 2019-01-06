__all__ = ('ModelComponent')


from pygame.math import Vector2
from pygame.surface import Surface


class ModelComponent:

    def __init__(self, position: Vector2, image: Surface):

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position

    @property
    def position(self) -> Vector2:

        return Vector2(self.rect.center)

    @position.setter
    def position(self, value: Vector2):

        self.rect.center = value

    def destroy(self):

        pass

    def update(self, *args):

        pass
