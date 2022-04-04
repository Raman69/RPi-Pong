from select import select
from sense_hat import SenseHat
import os
import pygame 
from pygame.locals import *
from time import sleep
def clear():
    matrix.clear()

def set_pixel(a,b,c):
    matrix.set_pixel(a,b,c)

matrix = SenseHat()
matrix.rotation = 180






