__all__ = ('TransformComponent',)


from pygame.math import Vector2


class TransformComponent:

    def __init__(self, direction: Vector2, speed: int):

        self.__direction = direction
        self.speed = speed

    @property
    def direction(self) -> Vector2:

        return self.__direction

    @direction.setter
    def direction(self, value: Vector2):

        self.x = value.x
        self.y = value.y

    @property
    def velocity(self) -> Vector2:

        return self.direction * self.speed

    @property
    def x(self) -> int:

        return self.direction.x

    @x.setter
    def x(self, value: int):

        nx = int(bool(value))
        if value < 0:
            nx *= -1
        self.direction.x = nx

    @property
    def y(self) -> int:

        return self.direction.y

    @y.setter
    def y(self, value: int):

        ny = int(bool(value))
        if value < 0:
            ny *= -1
        self.direction.y = ny

    def destroy(self):

        pass

    def update(self, *args):

        pass
