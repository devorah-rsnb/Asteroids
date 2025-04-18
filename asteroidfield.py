import pygame as pg
from random import uniform, choice, randint
from asteroid import Asteroid
from constants import *


class AsteroidField(pg.sprite.Sprite):
    edges = [
        {
            "direction" : DIR_RIGHT,
            "spawn_location" : lambda y: pg.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)
        },
        {
            "direction" : DIR_LEFT,
            "spawn_location" : lambda y: pg.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT)
        },
        {
            "direction" : DIR_UP,
            "spawn_location" : lambda x: pg.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS)
        },
        {
            "direction" : DIR_DOWN,
            "spawn_location" : lambda x: pg.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS)
        }
    ]

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0  

    def update(self, dt: int) -> None:
        self.spawn_timer += dt
        if self.spawn_timer <= ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

        # spawn a new asteroid at a random edge
        edge = choice(self.edges)
        cardinal_velocity = edge["direction"] * randint(ASTEROID_MAX_SPEED, ASTEROID_MIN_SPEED)
        velocity = cardinal_velocity.rotate(randint(-30, 30))
        position = edge["spawn_location"](uniform(0, 1))
        kind = randint(1, ASTEROID_KINDS)
        Asteroid(position.x, position.y, ASTEROID_MIN_RADIUS * kind, velocity)
