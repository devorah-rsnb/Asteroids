import pygame as pg
import sys
import json

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_BEZEL, FONT_SIZE, LINE_SPACING, HIGH_SCORE_PATH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def load_high_scores() -> list[int]:
    try:
        with open(HIGH_SCORE_PATH, 'r') as score_file:
            return json.load(score_file)
    except FileNotFoundError:
        return [0]

def draw_score(screen, font, score: int, high_scores: list[int]) -> None:
    high_score_surf = font.render(f"High Score: {high_scores[-1]}", True, "white")
    screen.blit(high_score_surf, screen.get_rect().inflate(SCREEN_BEZEL, SCREEN_BEZEL))
    score_surf = font.render(f"Score: {score}", True, "white")
    screen.blit(score_surf, screen.get_rect().inflate(SCREEN_BEZEL, SCREEN_BEZEL - FONT_SIZE * LINE_SPACING))

def save_high_scores(high_scores: list[int], new_score: int) -> None:
    high_scores.append(new_score)
    high_scores.sort()
    with open(HIGH_SCORE_PATH, 'w') as score_file:
        json.dump(high_scores, score_file)


def main() -> None:
    print("Starting Asteroids!")
    print(f"Screen size: {SCREEN_WIDTH} x {SCREEN_HEIGHT}")

    # Initialize pygame, boilerplate
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    font = pg.font.SysFont(None, FONT_SIZE)
    dt = 0 # Seconds since last frame
    score = 0

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

    high_scores = load_high_scores()

    while True:

        # Get all input, but handle it in player.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # Logic and Player input for upcoming frame
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                save_high_scores(high_scores, score)
                sys.exit()
            for shot in shots:
                if shot.is_collision(asteroid):
                    score += 1
                    asteroid.split()
                    shot.kill()
        
        # View
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)
        draw_score(screen, font, score, high_scores)
        pg.display.flip()

        # Seconds since last frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()