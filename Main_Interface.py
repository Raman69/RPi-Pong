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
    x,x,x,w,w,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,x,w,w,x,x,x,
    x,x,x,x,x,x,x,x
    ]) 
event = sense.stick.wait_for_event()
while event.direction != "up" and event.direction != "down":
    event = sense.stick.wait_for_event()
    joystick_event(event)
if event.action == "pressed" and event.direction == "up":
    sense.clear()
    exec(open(r"/home/raman/RPi-Pong/Multiplayer Pong/Multiplayer_server.py").read())
elif event.action == "pressed" and event.direction == "down":
    sense.clear()
    exec(open(r"/home/raman/RPi-Pong/Multiplayer Pong/Multiplayer_client.py").read())
