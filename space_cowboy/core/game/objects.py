__all__ = (
    'PlayerShip',
)


from pygame.math import Vector2


class PlayerShip:

    def __init__(self, input_component):

        super().__init__()
        self.__input_component = input_component
        self.direction = Vector2(0, 0)

    def update(self):

        self.__input_component.update(self)

    def move(self, direction: Vector2):

        self.direction = direction
