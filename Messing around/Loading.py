import random 
from LEDmatrix import *
import time
from sense_hat import SenseHat

clear()

while True:
    set_pixel(0,0,[0,0,255])
    set_pixel(1,0,[0,0,255])
    set_pixel(0,i+1,[0,0,255])
    set_pixel(1,i+1,[0,0,255])
    delay(1)
    clear()