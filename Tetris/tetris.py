#start of imports
import random 
from LEDmatrix import *
import time
from sense_hat import SenseHat

#end of imports
clear()

#colours

#cyan
c = [0, 204, 255]
#yellow
y = [255, 255, 0]
#red
r = [255,0,0] 
#greeen
g = [0,255,0]
#pink
p = [204, 0, 255]

#shortened things cus why not
sp = set_pixel
sense = SenseHat()


#The x and y coords at the start (cus the whole thing is 8x8)
x = 5
y = 3



#square def (yellow)
def square():
    sp(x,y,y)
    sp(x+1,y,y)
    sp(x+1,y+1,y)
    sp(x,y+1,y)


#line def (cyan)
def line():
    sp(x,y,c)
    sp(x,y+1,c)
    sp(x,y+2,c)
    sp(x,y+3,c)


#def t shape (pink)
def T():
    sp(x,y,p)
    sp(x+1,y,p)
    sp(x+1,y+1,p)
    sp(x+1,y-1,p)


#idk what to call this one
#def weird shape (green)
def weird():

    sp(x,y,g)
    sp(x+1,y,g)
    sp(x+1,y-1,g)
    sp(x+2,y-1,g)


#L shape def (red/orange)
def L():
    sp(x,y,r)
    sp(x,y+1,r)
    sp(x+1,y,r)
    sp(x+2,y,r)




#main loop
while True:
    clear()
    #gravity
    while True:
        time.sleep(1)
        if x == 0:
            break
        else:
            x = x-1

            
    #movement left and right (joystick shit)


    while True:
        for event in sense.stick.get_events():
            direction = event.direction
            print(event.direction)
            if direction == "up" :
                print("right")
                y = y-1
                print(y)
            elif direction == "down":
                print("left")
                y = y+1
                print(y)
            
            clear()
            T()





    









