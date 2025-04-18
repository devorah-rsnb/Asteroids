import pygame as pg

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Cardinal directions; easier to use if declared explicitly
DIR_UP = pg.Vector2(0,1)
DIR_DOWN = pg.Vector2(0,-1)
DIR_RIGHT = pg.Vector2(1,0)
DIR_LEFT = pg.Vector2(-1,0)

# All objects are polygons, so their line width needs to be defined
STROKE_WIDTH = 2 # mm?

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
SPLIT_ACCELERATION = 1.2 # px/s/s

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200

SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

SPLIT_MIN_ANGLE = 20
SPLIT_MAX_ANGLE = 50