import pygame as pg
from random import uniform

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SPLIT_ACCELERATION, SPLIT_MIN_ANGLE, SPLIT_MAX_ANGLE


class Asteroid(CircleShape):
    def __init__(self, position: pg.Vector2, radius: int, velocity: pg.Vector2):
        super().__init__(position, radius, velocity)
    
    def split(self) -> None:
        self.kill() # Remove self from asteroids, updatable and drawable groups
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 

        angle = uniform(SPLIT_MIN_ANGLE, SPLIT_MAX_ANGLE)
        velocity1 = self.velocity.rotate(angle) * SPLIT_ACCELERATION
        velocity2 = self.velocity.rotate(-angle) * SPLIT_ACCELERATION
        new_r = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position, new_r, velocity1)
        Asteroid(self.position, new_r, velocity2)
