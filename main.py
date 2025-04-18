import pygame as pg
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main() -> None:
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
        for _ in pg.event.get(): pass

        # Logic and Player input for upcoming frame
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.is_collision(asteroid):
                    asteroid.split()
                    shot.kill()
        
        # View
        pg.Surface.fill(screen, "black")
        for drawable in drawables:
            drawable.draw(screen)
        pg.display.flip()

        # Seconds since last frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()