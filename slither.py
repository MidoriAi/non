import pygame as pg
from pygame.locals import *
import random, sys

pg.init()

W = 640
HW = W//2
s = pg.display.set_mode((W, W))
pg.display.set_caption("Slither")
clock = pg.time.Clock()

BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
def color_generator(): return [(random.randint(50, 255)) for _ in range(3)]

bg = pg.image.load('hex_gray.jpg').convert()

right = True
left = False
up = False
down = False

class Worm:
    def __init__(self, x, y, color, radius, speed=5, worm_type=1):
        self.x = x
        self.y = y
        self.worm_type = worm_type
        self.color = color
        self.radius = radius
        self.speed = speed
        self.segments = []


    def create_worm(self):
        if self.worm_type:
            starting_pos = [(HW+i*-self.radius, HW) for i in range(12)]
            for pos in starting_pos:
                seg_rect = pg.Rect(pos, (self.radius, self.radius))
                self.segments.append(seg_rect)

    def move(self):
        if self.worm_type:
            global right, left, up, down
            for seg in range(len(self.segments) - 1, 0, -1):
                pg.draw.circle(s, self.color, (self.segments[seg].x, self.segments[seg].y), self.radius)
                new_x = self.segments[seg - 1].x
                new_y = self.segments[seg - 1].y
                self.segments[seg].x = new_x
                self.segments[seg].y = new_y

            keys = pg.key.get_pressed()
            if keys[K_RIGHT]: right, left, up, down = True, False, False, False
            if keys[K_LEFT]: right, left, up, down = False, True, False, False
            if keys[K_UP]: right, left, up, down = False, False, True, False
            if keys[K_DOWN]: right, left, up, down = False, False, False, True

            if right: self.segments[0].x += self.speed
            if left: self.segments[0].x -= self.speed
            if up: self.segments[0].y -= self.speed
            if down: self.segments[0].y += self.speed


my_worm = Worm(HW, HW, color_generator(), 10)
my_worm.create_worm()
anima_worm = Worm(100, 100, color_generator(), 15)
anima_worm.create_worm()

while True:
    s.fill(BLACK)
    s.blit(bg, (0, 0))
    my_worm.move()
    anima_worm.move()

    for e in pg.event.get():
        if e.type == QUIT:
            pg.quit()
            sys.exit()
    pg.display.update()
    clock.tick(60)

# Todo 2: -- MAKE THE BG SCROLL & THE HEAD ALWAYS AT THE CENTER SORTA LIKE A CAMERA FOLLOWING --
#

# Todo 1: -- CREATE THE 1st WORM WITH CLASSES & MAKE IT MOVE --
# ... done



# ***** THOUGHTS *****
# i think i'll initially make the AI worms to just go in a random SINGLE direction
