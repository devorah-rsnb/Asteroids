import pygame as pg

from circleshape import CircleShape
from constants import STROKE_WIDTH, DIR_UP, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOOT_SPEED, SHOOT_COOLDOWN
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shoot_timer = 0
        self.direction = DIR_UP

    def triangle(self) -> list[pg.Vector2, pg.Vector2, pg.Vector2]:
        width = self.direction.rotate(90) * self.radius / 1.5
        a = self.position + self.direction * self.radius
        b = self.position - self.direction * self.radius - width
        c = self.position - self.direction * self.radius + width
        return [a, b, c]
    
    def draw(self, screen) -> None:
         pg.draw.polygon(screen, "white", self.triangle(), STROKE_WIDTH)
    
    def rotate(self, dt: int) -> None:
        self.direction = self.direction.rotate(PLAYER_TURN_SPEED * dt)
    
    def move(self, dt: int) -> None:
        self.position += self.direction * PLAYER_SPEED * dt
    
    def update(self, dt: int) -> None:
        keys = pg.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pg.K_a]: self.rotate(-dt)
        if keys[pg.K_d]: self.rotate(dt)
        if keys[pg.K_w]: self.move(dt)
        if keys[pg.K_s]: self.move(-dt)
        if keys[pg.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
        
    def shoot(self) -> None:
        Shot(self.position.x, self.position.y, self.direction * SHOOT_SPEED)
        self.shoot_timer = SHOOT_COOLDOWN
