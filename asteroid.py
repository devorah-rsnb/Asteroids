import pygame as pg
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SPLIT_MIN_ANGLE, SPLIT_MAX_ANGLE

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int, velocity: pg.Vector2):
        super().__init__(x, y, radius, velocity)
    
    def split(self) -> None:
        self.kill() # Remove self from asteroids, updatable and drawable groups
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            angle = random.uniform(SPLIT_MIN_ANGLE, SPLIT_MAX_ANGLE)
            velocity1 = self.velocity.rotate(angle) * 1.2
            velocity2 = self.velocity.rotate(-angle) * 1.2
            new_r = self.radius - ASTEROID_MIN_RADIUS
            A1 = Asteroid(self.position.x, self.position.y, new_r, velocity1)
            A2 = Asteroid(self.position.x, self.position.y, new_r, velocity2)
