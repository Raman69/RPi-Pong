#start of imports
from random import randint
from LEDmatrix import *
import time
#end of imports
clear()

#color and shortening
white = [255,255,255]
#sp to save time(this is gonna be used alot)
sp = set_pixel

#The x and y coords at the start (cus the whole thing is 8x8)
x = 8
y = 3 

#square def
def square():
    sp(x,y,white)
    sp(x+1,y,white)
    sp(x+1,y+1,white)
    sp(x,y+1,white)


#line def 
def line():
    sp(x,y,white)
    sp(x,y+1,white)
    sp(x,y+2,white)
    sp(x,y+3,white)


#def t shape
def T():
    sp(x,y,white)
    sp(x+1,y,white)
    sp(x+1,y+1,white)
    sp(x+1,y-1,white)


#idk what to call this one
#def weird shape
def weird():
    sp(x,y,white)
    sp(x+1,y,white)
    sp(x+1,y-1,white)
    sp(x+2,y-1,white)


#L shape def
def L():
    sp(x,y,white)
    sp(x,y+1,white)
    sp(x+1,y,white)
    sp(x+2,y,white)

#gravity (will just x-1 every second)
while True:
    time.sleep(1)
    if x == 0:
        break
    else:
        x-1
weird()

    









