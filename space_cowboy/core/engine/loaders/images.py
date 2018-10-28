__all__ = ('ImagesLoader',)


import os
from pygame.image import load
from pygame.locals import RLEACCEL
from pygame.surface import Surface
from ..typedefs import ColorKey


class ImagesLoader:

    def __init__(self, assets_path: str):

        self.assets_path = assets_path


    def load_image(self, file_path: str) -> Surface:

        return load(os.path.join(self.assets_path, file_path))


    def load_image_surface(self, file_path: str, color_key: ColorKey = None) -> Surface:

        image = self.load_image(file_path).convert()
        if color_key is not None:
            image = self.set_colorkey(image, color_key)
        return image


    def load_image_surface_alpha(self, file_path: str) -> Surface:

        image = self.load_image(file_path).convert_alpha()
        return image


    def set_colorkey(self, image: Surface, color_key: ColorKey) -> Surface:

        if color_key is -1:
            return image.set_colorkey(image.get_at((0, 0)), RLEACCEL)
        return image.set_colorkey(color_key, RLEACCEL)
