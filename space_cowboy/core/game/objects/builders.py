__all__ = (
    'build_player_ship',
)


import os
from typing import Iterable

from pygame.math import Vector2

from ...loaders.images import ImagesLoader
from ..components.input import PlayerInputComponent
from ..components.sprite import SpriteComponent
from .objects import PlayerShip


def build_player_ship(position: Iterable, direction: Iterable, velocity: int, images_loader: ImagesLoader,
                      input_component: PlayerInputComponent) -> PlayerShip:

    try:
        dir_vec = Vector2(direction).normalize_ip()
    except ValueError:
        dir_vec = Vector2(0, 0)

    image = images_loader.load_surface_alpha(
        os.path.join('ships', 'ship1_red.png'))
    sprite_component = SpriteComponent(Vector2(position), image)

    return PlayerShip(dir_vec, velocity, sprite_component, input_component)
