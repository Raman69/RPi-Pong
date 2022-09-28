from sense_hat import SenseHat
import os
from time import sleep
from signal import pause

sense = SenseHat()
x = (0, 0, 0)
w = (255, 255, 255)

def joystick_event(event):
    print("The joystick was {} {}".format(event.action, event.direction))

sense.set_pixels([
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,w,x,x,x,x,w,x,
    x,w,x,x,x,x,w,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x
    ]) 

event = sense.stick.wait_for_event()
while event.direction != "right" and event.direction != "left":
    event = sense.stick.wait_for_event()
    joystick_event(event)

if event.action == "pressed" and event.direction == "right":
    #code to run in tetris mode
    sense.set_pixels([
        x,x,x,x,x,x,x,x,
        x,w,w,w,w,w,w,x,
        x,w,w,w,w,w,w,x,
        x,x,x,w,w,x,x,x,
        x,x,x,w,w,x,x,x,
        x,x,x,w,w,x,x,x,
        x,x,x,w,w,x,x,x,
        x,x,x,x,x,x,x,x
        ]) 
elif event.action == "pressed" and event.direction == "left":
    #code to run in pong mode
    sense.set_pixels([
        x,x,x,x,x,x,x,x,
        x,x,x,w,w,x,x,x,
        x,x,x,x,x,x,x,x,
        x,x,x,x,x,x,x,x,
        x,x,x,x,x,x,x,x,
        x,x,x,x,x,x,x,x,
        x,x,x,w,w,x,x,x,
        x,x,x,x,x,x,x,x
        ]) 

    while event.direction != "up" and event.direction != "down":
        event = sense.stick.wait_for_event()
        joystick_event(event)

    if event.action == "pressed" and event.direction == "up":
        sense.clear()
        os.system('python /home/pi/RPi-Pong/RPi-Pong/Multiplayer_Pong/Multiplayer_server.py')
    elif event.action == "pressed" and event.direction == "down":
        sense.clear()
        os.system('python /home/pi/RPi-Pong/RPi-Pong/Multiplayer_Pong/Multiplayer_client.py')
