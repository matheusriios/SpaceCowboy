__all__ = ('SoundsHandler',)


import os
from pygame.mixer import Sound


class SoundsHandler:

    def __init__(self, assets_path: str):

        self.assets_path = assets_path


    def load_sound(self, file_path: str) -> Sound:

        path = os.path.join(self.assets_path, file_path)
        sound = Sound(path)
        return sound
