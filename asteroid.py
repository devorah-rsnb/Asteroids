import pygame as pg
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SPLIT_MIN_ANGLE, SPLIT_MAX_ANGLE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pg.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            angle = random.uniform(SPLIT_MIN_ANGLE, SPLIT_MAX_ANGLE)
            velocity1 = self.velocity.rotate(angle)
            velocity2 = self.velocity.rotate(-angle)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            A1 = Asteroid(self.position.x, self.position.y, new_r)
            A1.velocity = velocity1 * 1.2
            A2 = Asteroid(self.position.x, self.position.y, new_r)
            A2.velocity = velocity2 * 1.2
