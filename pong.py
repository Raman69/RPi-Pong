from select import select
from sense_hat import SenseHat
import os
import pygame 
from pygame.locals import *
from time import sleep


matrix = SenseHat()
matrix.rotation = 180
matrix.lowlight = True


def set_pixel(a,b,c):
    matrix.set_pixel(a,b,c)

def ball():
    set_pixel(1,1,[0,0,255])


def clear():
    matrix.clear()


def ballm():
    while True:
        for i in range(0,8):
            clear()
            set_pixel(i,i,[0,0,255])
            sleep(0.05)















