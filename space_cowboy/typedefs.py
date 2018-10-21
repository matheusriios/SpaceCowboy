__all__ = (
    'Colorkey',
    'Event',
    'ScreenSize',
)


from typing import (
    Tuple,
)
from pygame.event import (
    EventType,
)


Colorkey = Tuple[int, int, int]
Event = EventType
ScreenSize = Tuple[int, int]
