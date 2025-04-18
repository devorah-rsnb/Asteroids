import pygame as pg

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, position: pg.Vector2, velocity: pg.Vector2):
        super().__init__(position, SHOT_RADIUS, velocity)
