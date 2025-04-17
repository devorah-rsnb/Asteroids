import pygame as pg
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen size: {SCREEN_WIDTH} x {SCREEN_HEIGHT}")

    # Initialize pygame, boilerplate
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0 # Seconds since last frame

    # Class accessible containers that allow objects to destruct themselves
    updatable = pg.sprite.Group()
    drawables = pg.sprite.Group()  
    asteroids = pg.sprite.Group() 
    shots = pg.sprite.Group() 

    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawables)

    # This object implicitly manages the asteroids as an 'updatable' object
    asteroid_field = AsteroidField()

    # Player in center of window to start
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        # Get all input, but handle it in player.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        pg.Surface.fill(screen, (0, 0, 0))

        # Logic and Player input for upcoming frame
        updatable.update(dt)

        # Check for collisions
        for item in asteroids:
            if item.is_collision(player):
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.is_collision(item):
                    item.split()
                    bullet.kill()
        
        # View
        for item in drawables:
            item.draw(screen)
        pg.display.flip()

        # Seconds since last frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()