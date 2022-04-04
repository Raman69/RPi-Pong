from select import select
from sense_hat import SenseHat
import os
import pygame 
from pygame.locals import *
from time import sleep
matrix = SenseHat()
matrix.rotation = 180

def clear():
    matrix.clear()

def set_pixel(a,b,c):
    matrix.set_pixel(a,b,c)













