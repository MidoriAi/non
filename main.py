import pygame as pg
from pygame.locals import *
import random, sys

pg.init()

W = 800
M = W//2
s = pg.display.set_mode((W, W))
clock = pg.time.Clock()

BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
radius = 10
speed = 5
starting_pos = [(M+i*-radius, M) for i in range(7)]
segments = []
for pos in starting_pos:
    segment_rect = pg.Rect(pos, (radius, radius))
    segments.append(segment_rect)

def color_generator(): return [(random.randint(100, 255)) for _ in range(3)]
color = color_generator()

while True:
    s.fill(BLACK)
    for seg in range(len(segments)-1, 0, -1):
        # segment = pg.draw.rect(s, WHITE, segments[seg], 2)
        segment = pg.draw.circle(s, color, (segments[seg].x, segments[seg].y), radius, 2)
        new_x = segments[seg - 1].x
        new_y = segments[seg - 1].y
        segments[seg].x = new_x
        segments[seg].y = new_y

    mouse_pos = pg.mouse.get_pos()
    if segments[0].x > mouse_pos[0]: segments[0].x -= speed
    if segments[0].x < mouse_pos[0]: segments[0].x += speed
    if segments[0].y > mouse_pos[1]: segments[0].y -= speed
    if segments[0].y < mouse_pos[1]: segments[0].y += speed

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    clock.tick(40)

# === Step 3 KEEP THE WORM HEAD AT THE CENTER ===
#

# === Step 2 MAKING THE SCREEN SCROLL ===
# download an bg img
# move the bg to the direction of the worm by incrementing its coords every time the worm moves
# regenerate a new bg when the other bg's edges are visible to seem like a infinite world

# === Step 1 CREATING THE FIRST WORM ===
# make the square version of the worm with only 7 starting segments
# starting at the last segment, last segment should go to the coords of the 2nd to the last segment then the 2nd to the last segment go to the coords of the head
#  - this is done by getting the coords of the 2nd to the last segment then assigning the segment u wanna move to that coords
# make the worm follow the mouse & try the circle version of the worm