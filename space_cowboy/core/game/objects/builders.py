__all__ = (
    'build_player_ship',
)


import os
from typing import Iterable

from pygame.math import Vector2

from ...loaders.images import ImagesLoader
from ..components.input import PlayerInputComponent
from .objects import PlayerShip


def build_player_ship(position: Iterable, direction: Iterable, velocity: int, images_loader: ImagesLoader,
                      input_component: PlayerInputComponent) -> PlayerShip:

    pos_vec = Vector2(position)
    try:
        dir_vec = Vector2(direction).normalize_ip()
    except ValueError:
        dir_vec = Vector2(0, 0)
    image = images_loader.load_surface_alpha(
        os.path.join('ships', 'ship1_red.png'))
    return PlayerShip(pos_vec, dir_vec, velocity, image, input_component)
