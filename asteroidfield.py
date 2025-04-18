import pygame as pg
from random import uniform, choice, randint
from asteroid import Asteroid
from constants import *


class AsteroidField(pg.sprite.Sprite):
    edges = [
        [
            DIR_RIGHT,
            lambda y: pg.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            DIR_LEFT,
            lambda y: pg.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            DIR_UP,
            lambda x: pg.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            DIR_DOWN,
            lambda x: pg.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0

    def spawn(self, radius: int, position: pg.Vector2, velocity: pg.Vector2) -> None:
        asteroid = Asteroid(position.x, position.y, radius, velocity)

    def update(self, dt: int) -> None:
        self.spawn_timer += dt
        if self.spawn_timer <= ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

        # spawn a new asteroid at a random edge
        edge = choice(self.edges)
        speed = randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(randint(-30, 30))
        position = edge[1](uniform(0, 1))
        kind = randint(1, ASTEROID_KINDS)
        self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)