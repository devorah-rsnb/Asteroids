import pygame as pg

from circleshape import CircleShape
from constants import STROKE_WIDTH, DIR_UP, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.direction = DIR_UP

    def triangle(self) -> list[pg.Vector2, pg.Vector2, pg.Vector2]:
        right = DIR_UP.rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + self.direction * self.radius
        b = self.position - self.direction * self.radius - right
        c = self.position - self.direction * self.radius + right
        return [a, b, c]
    
    def draw(self, screen) -> None:
         pg.draw.polygon(screen, "white", self.triangle(), STROKE_WIDTH)
    
    def rotate(self, dt: int) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
        self.direction = DIR_UP.rotate(self.rotation)
    
    def move(self, dt: int) -> None:
        self.position += self.direction * PLAYER_SPEED * dt
    
    def update(self, dt: int) -> None:
        keys = pg.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pg.K_a]:
            self.rotate(-dt)
        if keys[pg.K_d]:
            self.rotate(dt)
        if keys[pg.K_w]:
            self.move(dt)
        if keys[pg.K_s]:
            self.move(-dt)
        if keys[pg.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot()
        
    def shoot(self) -> None:
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = self.direction * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
