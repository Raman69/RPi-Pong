from select import select
from sense_hat import SenseHat
from sense_hat import SenseHat
import os
import pygame 
from pygame.locals import *
from time import sleep


matrix = SenseHat()
matrix.rotation = 180
matrix.lowlight = True

def delay(t):
    sleep(t)

def clear():
    matrix.clear()

def fill(a):
    matrix.clear(a)

def set_pixel(a,b,c):
    matrix.set_pixel(a,b,c)

def display_pixels(a):
    matrix.set_pixels(a)

def display_image(a):
    matrix.load_image(a)


def use_joystick():
    pygame.init()
    pygame.display.set_mode((100, 100)).fill((0,255,0))
    pygame.display.flip()

def get_position():
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_DOWN:
                return "up"
            elif event.key == pygame.K_UP:
                return "down"
            elif event.key == pygame.K_LEFT:
                return "right"
            elif event.key == pygame.K_RIGHT:
                return "left"
            elif event.key == pygame.K_RETURN:
                return "centre"
            elif event.key == pygame.K_ESCAPE:
                return "escape"

def get_orientation(axis):
    o = matrix.get_orientation()
    Axis = o[axis]
    Axis = int(round(Axis,0))
    Axis = Axis + 90
    Axis = Axis % 360
    return Axis


