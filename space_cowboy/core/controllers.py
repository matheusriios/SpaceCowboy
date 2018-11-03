__all__ = ('GameController',)


from typing import Iterable
from pygame.event import Event
from pygame.locals import QUIT
from pygame.sprite import Group
from pygame.surface import Surface
from .loaders import ImagesLoader


class GameController:

    def __init__(self, display: Surface, images_loader: ImagesLoader):

        self.__background = None
        self.__display = display
        self.__sprites_list = Group()
        self.__images_loader = images_loader


    def process_events(self, events: Iterable[Event]):

        for event in events: # type: Event
            if event.type == QUIT:
                return True

        return False


    def process_updates(self):

        self.__sprites_list.update()


    def render_frame(self):

        self.__sprites_list.clear(self.__display, self.__background)
        self.__sprites_list.draw(self.__display)
