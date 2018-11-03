__all__ = ('ImagesLoader',)


import os
from pygame.image import load
from pygame.locals import RLEACCEL
from pygame.surface import Surface
from pygame.transform import smoothscale
from ..typedefs import (
    ColorKey,
    ScreenSize,
)


class ImagesLoader:

    def __init__(self, assets_path: str):

        self.assets_path = assets_path


    def __load(self, file_path: str) -> Surface:

        return load(os.path.join(self.assets_path, file_path))


    def load_surface(self, file_path: str, color_key: ColorKey = None) -> Surface:

        image = self.__load(file_path).convert()
        if color_key is not None:
            image = self.set_colorkey(image, color_key)
        return image


    def load_surface_alpha(self, file_path: str) -> Surface:

        image = self.__load(file_path).convert_alpha()
        return image


    def smoothscale(self, image: Surface, target_resolution: ScreenSize) -> Surface:

        return smoothscale(image, target_resolution)


    def set_colorkey(self, image: Surface, color_key: ColorKey) -> Surface:

        if color_key is -1:
            return image.set_colorkey(image.get_at((0, 0)), RLEACCEL)
        return image.set_colorkey(color_key, RLEACCEL)
