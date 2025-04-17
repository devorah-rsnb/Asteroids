import pygame as pg

# Base class for game objects
class CircleShape(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int):
        # Place reference of itself into container to be managed
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen) -> None:
        # sub-classes must override
        pass

    def update(self, dt: int) -> None:
        # sub-classes must override
        pass

    def is_collision(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        total_r = self.radius + other.radius
        return distance <= total_r
