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

#shapes = [["square", 2, 2]]
#y_axis = 7
#y_axis = shapes[0,2]

#shortened things cus why not
sp = set_pixel
sense = SenseHat()


#The x and y coords at the start (cus the whole thing is 8x8)
x_axies = 5
y_axies = 3
#the current shape being used
current_shape = ""



#square def (yellow)
def square():
    sp(x_axies,y_axies,y)
    sp(x_axies+1,y_axies,y)
    sp(x_axies+1,y_axies+1,y)
    sp(x_axies,y_axies+1,y)
    current_shape = "square"


#line def (cyan)
def line():
    sp(x_axies,y_axies,c)
    sp(x_axies,y_axies+1,c)
    sp(x_axies,y_axies+2,c)
    sp(x_axies,y_axies+3,c)
    current_shape = "line"


#def t shape (pink)
def T():
    sp(x_axies,y_axies,p)
    sp(x_axies+1,y_axies,p)
    sp(x_axies+1,y_axies+1,p)
    sp(x_axies+1,y_axies-1,p)
    current_shape = "T"


#idk what to call this one
#def weird shape (green)
def weird():

    sp(x_axies,y_axies,g)
    sp(x_axies+1,y_axies,g)
    sp(x_axies+1,y_axies+1,g)
    sp(x_axies+2,y_axies+1,g)
    current_shape = "weird"


#L shape def (red/orange)
def L():
    sp(x_axies,y_axies,r)
    sp(x_axies,y_axies-1,r)
    sp(x_axies+1,y_axies,r)
    sp(x_axies+2,y_axies,r)
    current_shape = "L"





    

#main loop[]           


while True:
    square()
    #gravity
    #while True:
        #time.sleep(1)
        #if x_axies == 0:
            #break
        #else:
            #x_axies = x_axies-1
    #movement left and right (joystick shit)
    for event in sense.stick.get_events():
        direction = event.direction
        event = event.action
        print(direction)
        if direction == "up" and event == "pressed" and current_shape == "square" or "T" or "weird" and y_axies == 6:
            pass
        elif direction == "down" and event == "pressed" and current_shape == "l" and y_axies == 0:
            pass
        elif direction == "up" and event == "pressed" :
            print("right")
            y_axies = y_axies-1
            print(y_axies)
        elif direction == "down" and event == "pressed":
            print("left")
            y_axies = y_axies+1
            print(y_axies)
        


                
            
        clear()
        





    









