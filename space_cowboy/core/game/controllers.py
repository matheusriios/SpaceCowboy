__all__ = ('GameController',)


from ..systems.events import EventSystem
from .components.input import PlayerInputComponent
from .objects import PlayerShip


class GameController:

    def __init__(self, event_system: EventSystem):

        self.__event_system = event_system
        self.__player = PlayerShip(PlayerInputComponent(self.__event_system))

    def process_events(self):

        self.__event_system.update()

    def update(self):

        self.__player.update()
