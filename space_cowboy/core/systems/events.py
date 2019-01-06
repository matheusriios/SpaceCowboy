"""
This module provides classes and functions to interface with the PyGame Event Queue.
"""


__all__ = (
    'EventSystem',
)


from typing import (
    Any,
    Callable,
    Iterable,
    Iterator,
    Union,
)
from pygame.event import (
    EventType,
    get,
    post,
    set_allowed,
    set_blocked,
)
from pygame.locals import (
    ACTIVEEVENT,
    JOYAXISMOTION,
    JOYBALLMOTION,
    JOYBUTTONDOWN,
    JOYBUTTONUP,
    JOYHATMOTION,
    KEYDOWN,
    KEYUP,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
    QUIT,
    USEREVENT,
    VIDEOEXPOSE,
    VIDEORESIZE,
)


class EventSystem:
    """
    EventSystem is a class that wraps the PyGame Event Queue and provides services
    such as an observer/observable pattern for better management of events using channels.
    """

    _event_types = (ACTIVEEVENT, JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN, JOYBUTTONUP, JOYHATMOTION, KEYDOWN,
                    KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION, QUIT, USEREVENT, VIDEOEXPOSE, VIDEORESIZE)

    def __init__(self):

        self.__channels = {event: {} for event in self._event_types}

    @staticmethod
    def post_event(events: Union[EventType, Iterable[EventType]]):
        """
        Post an event or a list of events at the end of the PyGame Event Queue.

        :param events: event or list of events to post.
        """
        try:
            for event in events:
                post(event)
        except TypeError:
            post(event)

    @staticmethod
    def set_allowed(event_types: Union[int, Iterable[int], None]):
        """
        Controls which events types are allowed in the queue.

        :param event_types: event type or list of event types to allow in the queue. If None, block any event.
        """
        set_allowed(event_types)

    @staticmethod
    def set_blocked(event_types: Union[int, Iterable[int], None]):
        """
        Controls which events types are block in the queue.

        :param event_types: event type or list of event types to block in the queue. If None, allow any event.
        """
        set_blocked(event_types)

    def clear_channel(self, event_types: Union[int, Iterable[int]]):
        """
        Clear a channel from subscribers.

        :param event_types: event type or list of event types to clear related channels.
        """
        try:
            for type_ in event_types:
                self.__channels[type_] = dict()
        except TypeError:
            self.__channels[event_types] = dict()

    def subscribe(self, subscriber: Any, callback: Callable[[EventType], Any],
                  event_types: Union[int, Iterable[int]] = None):
        """
        Subscribe to a channel, informing a callback to be executed when the event is detected in the queue.

        :param subscriber: object that is subscribing.
        :param callback: callback function to be executed when an event of event_type is detected in the queue.
        :param event_types: event type or list of types to subscribe to. If None, subscribes to every channel.
        """
        if event_types:
            try:
                for type_ in event_types:
                    self.__channels[type_][subscriber] = callback
            except TypeError:
                type_ = event_types
                self.__channels[type_][subscriber] = callback
        else:
            for chn in self.__channels:
                self.subscribe(subscriber, callback, chn)

    def unsubscribe(self, subscriber: Any, event_types: Union[int, Iterable[int]] = None):
        """
        Unsubscribe from a given event channel or every channel.

        :param subscriber: object that is unsubscribing.
        :param event_types: event type or list of types to unsubscribe to. If None, unsubscribes from every channel.
        """

        if event_types:
            try:
                for type_ in event_types:
                    self.__channels[type_].pop(subscriber, None)
            except TypeError:
                type_ = event_types
                self.__channels[type_].pop(subscriber, None)
        else:
            for chn in self.__channels:
                self.unsubscribe(subscriber, chn)

    def update(self):
        """
        Utility function to run every tick. Iterates through events list and execute registered callbacks for each
        event channel.
        """
        events: Iterator[EventType] = get()
        for event in events:
            for callback in self.__channels[event.type].values():
                callback(event)
