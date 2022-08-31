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
x_axies = 5
y_axies = 3



#square def (yellow)
def square():
    sp(x_axies,y_axies,y)
    sp(x_axies+1,y_axies,y)
    sp(x_axies+1,y_axies+1,y)
    sp(x_axies,y_axies+1,y)


#line def (cyan)
def line():
    sp(x_axies,y_axies,c)
    sp(x_axies,y_axies+1,c)
    sp(x_axies,y_axies+2,c)
    sp(x_axies,y_axies+3,c)


#def t shape (pink)
def T():
    sp(x_axies,y_axies,p)
    sp(x_axies+1,y_axies,p)
    sp(x_axies+1,y_axies+1,p)
    sp(x_axies+1,y_axies-1,p)


#idk what to call this one
#def weird shape (green)
def weird():

    sp(x_axies,y_axies,g)
    sp(x_axies+1,y_axies,g)
    sp(x_axies+1,y_axies-1,g)
    sp(x_axies+2,y_axies-1,g)


#L shape def (red/orange)
def L():
    sp(x_axies,y_axies,r)
    sp(x_axies,y_axies+1,r)
    sp(x_axies+1,y_axies,r)
    sp(x_axies+2,y_axies,r)





    

            
    #movement left and right (joystick shit)

while True:
    T()
    while True:
        time.sleep(1)
        if x_axies == 0:
            break
        else:
            x_axies = x_axies-1
    for event in sense.stick.get_events():
        direction = event.direction
        print(event.direction)
        if direction == "up" :
            print("right")
            y_axies = y_axies-1
            print(y_axies)
        elif direction == "down":
            print("left")
            y_axies = y_axies+1
            print(y_axies)
            
        clear()
        





    









