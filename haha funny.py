from select import select
from sense_hat import SenseHat
import os
import pygame 
from pygame.locals import *
from time import sleep

matrix = SenseHat()

def display_pixels(a):
    matrix.set_pixels(a)

def display_image(a):
    matrix.load_image(a)


B = [0,0,255]
R = [255,0,0]
G = [0,255,0]
O = [255,165,0]
Y = [255,255,0]
P = [128,0,128]
I = [75,0,130]
X = [0,0,0]

smiley = [
    X,X,X,X,X,X,X,X,
    X,X,X,I,I,X,X,X,
    X,X,X,P,P,X,X,X,
    X,X,X,B,B,X,X,X,
    X,X,X,G,G,X,X,X,
    X,X,X,Y,Y,X,X,X,
    X,O,O,X,X,O,O,X,
    X,R,R,X,X,R,R,X
    ]
display_pixels(smiley)