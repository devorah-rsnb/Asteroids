import pygame as pg
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()  
    asteroids = pg.sprite.Group() 
    shots = pg.sprite.Group() 

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.Surface.fill(screen, (0, 0, 0))
        updatable.update(dt)
        for item in asteroids:
            if item.is_collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.is_collision(item):
                    item.split()
                    bullet.kill()
        for item in drawable:
            item.draw(screen)
        pg.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()