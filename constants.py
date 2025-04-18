import pygame as pg


# Pixels
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Cardinal directions; easier to use if declared explicitly
DIR_UP = pg.Vector2(0,1)
DIR_DOWN = pg.Vector2(0,-1)
DIR_RIGHT = pg.Vector2(1,0)
DIR_LEFT = pg.Vector2(-1,0)

# All objects are polygons, define their line width 
STROKE_WIDTH = 2 # Pixels, supposedly

ASTEROID_MAX_SPEED = 40 # px/s
ASTEROID_MIN_SPEED = 100 # px/s
ASTEROID_MIN_RADIUS = 20 # px
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS # px
SPLIT_ACCELERATION = 1.2 # px/s/s
SPAWN_DEFLECTION = 30 # degrees

PLAYER_RADIUS = 20 # px
PLAYER_TURN_SPEED = 300 # degrees/s
PLAYER_SPEED = 200 # px/s

SHOT_RADIUS = 5 # px
PLAYER_SHOOT_SPEED = 500 # px/s
PLAYER_SHOOT_COOLDOWN = 0.3 # shots/s

SPLIT_MIN_ANGLE = 20 # degrees
SPLIT_MAX_ANGLE = 50 # degrees
