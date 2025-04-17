import pygame as pg

# Base class for game objects
class CircleShape(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int, velocity: pg.Vector2 = pg.Vector2(0,0)):
        # Place reference of itself into container to be managed
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pg.Vector2(x, y)
        self.radius = radius
        self.velocity = velocity

    def draw(self, screen) -> None:
        pg.draw.circle(screen, "white", self.position, self.radius, 2)

    # Default frame action is Newton's 1st law
    def update(self, dt: int) -> None:
        self.position += self.velocity * dt

    def is_collision(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        total_r = self.radius + other.radius
        return distance <= total_r
