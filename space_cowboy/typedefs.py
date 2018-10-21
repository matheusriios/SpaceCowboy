__all__ = (
    'Colorkey',
    'Event',
)


from typing import (
    Tuple,
)
from pygame.event import (
    EventType,
)


Colorkey = Tuple[int, int, int]
Event = EventType
