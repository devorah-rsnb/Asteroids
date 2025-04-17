import pygame as pg

from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x: int, y: int, velocity: pg.Vector2):
        super().__init__(x, y, SHOT_RADIUS, velocity)
