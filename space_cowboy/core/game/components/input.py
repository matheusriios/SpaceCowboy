__all__ = ('KeyboardInputComponent',)


from typing import (
    Callable,
    Dict,
)

from pygame.event import EventType
from pygame.locals import (
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_UP,
    KEYDOWN,
    KEYUP,
)

from ...systems.events import EventSystem


Action = Callable[[dict], None]
ActionType = Dict[int, Action]
KeyAction = Dict[int, ActionType]


class KeyboardInputComponent:

    def __init__(self, event_system: EventSystem, key_action_map: KeyAction = {}):

        self.__event_system = event_system
        self.__key_action_map = key_action_map
        event_system.subscribe(self, self.__event_dispatcher, (KEYDOWN, KEYUP))

    @property
    def key_action_map(self) -> KeyAction:

        return self.__key_action_map

    def __event_dispatcher(self, event: EventType):

        key = event.key
        if key in self.__key_action_map:
            process = self.__key_action_map.get(key).get(event.type)
            if process:
                process(event)

    def clear_keys(self) -> 'KeyboardInputComponent':

        self.__key_action_map = {}
        return self

    def update_keys(self, key_action_map: KeyAction) -> 'KeyboardInputComponent':

        self.__key_action_map.update(key_action_map)
        return self

    def destroy(self):

        self.__event_system.unsubscribe(self)

    def update(self, *args):

        pass
