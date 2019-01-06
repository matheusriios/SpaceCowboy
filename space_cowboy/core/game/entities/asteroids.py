__all__ = ('Asteroid',)


from pygame.rect import Rect
from pygame.sprite import Sprite
from pygame.surface import Surface

from ..components.model import ModelComponent
from ..components.transform import TransformComponent


class Asteroid(Sprite):

    def __init__(self, mc: ModelComponent, tc: TransformComponent):

        super().__init__()
        self.__components = {
            'model_component': mc,
            'transform_component': tc
        }

    @property
    def image(self) -> Surface:

        return self.__components['model_component'].image

    @property
    def rect(self) -> Rect:

        return self.__components['model_component'].rect

    def destroy(self):

        for component in self.__components.values():
            component.destroy()
            del component

    def update(self, *args):

        for component in self.__components.values():
            component.update()

        mc = self.__components['model_component']
        tc = self.__components['transform_component']
        mc.position += tc.velocity
