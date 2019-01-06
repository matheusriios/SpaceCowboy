__all__ = ('build_player_ship',)


import os
from typing import Iterable

from pygame.math import Vector2

from ...systems.events import EventSystem
from ...loaders.images import ImagesLoader
from ..components.input import KeyboardInputComponent
from ..components.model import ModelComponent
from ..components.transform import TransformComponent
from .asteroids import Asteroid
from .ships import PlayerShip


def build_asteroid(position: Vector2, direction: Vector2, speed: int, images_loader: ImagesLoader) -> Asteroid:

    # Build model component
    image = images_loader.load_surface_alpha(
        os.path.join('asteroids', 'meteor_brown_med1.png'))
    mc = ModelComponent(position, image)

    # Build transform component
    tc = TransformComponent(direction, speed)

    return Asteroid(mc, tc)


def build_player_ship(position: Iterable, direction: Iterable, speed: int, event_system: EventSystem,
                      images_loader: ImagesLoader) -> PlayerShip:


    # Build input component
    ic = KeyboardInputComponent(event_system)

    # Build sprite component
    image = images_loader.load_surface_alpha(
        os.path.join('ships', 'ship1_red.png'))
    mc = ModelComponent(Vector2(position), image)

    # Build transform component
    try:
        dir_vec = Vector2(direction).normalize_ip()
    except ValueError:
        dir_vec = Vector2(0, 0)
    tc = TransformComponent(dir_vec, speed)

    return PlayerShip(ic, mc, tc)
