#the top of the 8x8 will have a white line 

from sense_hat import SenseHat
from LEDmatrix import *

sp = set_pixel

w = [255,255,255]
clear()


for i in range(1,7):
    sp(i,7,w)


