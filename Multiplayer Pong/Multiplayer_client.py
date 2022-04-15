from bluedot.btcomm import BluetoothClient
from time import sleep
from signal import pause
from sense_hat import SenseHat
import os

opp_bat_y = 4

# Defining sense HAT and clearing LED matrix
sense = SenseHat()
sense.clear()
sense.lowlight = True

white = (255, 255, 255)
blue = (0, 0, 255)
bat_y = 4
ball_position = [0, 0]
ball_velocity = [1, 1]
w = [255, 255, 255]
x = [0, 0, 0]
sad = [
    x,x,x,x,x,x,x,x,
    x,w,w,x,x,w,w,x,
    x,w,w,x,x,w,w,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,x,w,w,w,w,x,x,
    x,w,w,x,x,w,w,x,
    x,x,x,x,x,x,x,x
    ]
happy = [
    x,x,x,x,x,x,x,x,
    x,w,w,x,x,w,w,x,
    x,w,w,x,x,w,w,x,
    x,x,x,x,x,x,x,x,
    x,x,x,x,x,x,x,x,
    x,w,w,x,x,w,w,x,
    x,x,w,w,w,w,x,x,
    x,x,x,x,x,x,x,x
    ]

# Functions
def draw_bat():
    global opp_bat_y
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y - 1, white)
    sense.set_pixel(7, opp_bat_y + 1, white)
    sense.set_pixel(7, opp_bat_y, white)
    sense.set_pixel(7, opp_bat_y - 1, white)


def draw_ball():
    global opp_bat_y
    sense.set_pixel(ball_position[0], ball_position[1], blue)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]

    if ball_position[0] == 6 and (opp_bat_y - 2) <= ball_position[1] <= (opp_bat_y + 2):
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[0] == 1 and (bat_y - 2) <= ball_position[1] <= (bat_y + 2):
        ball_velocity[0] = -ball_velocity[0]

    if ball_position[0] == 0:
        sense.set_pixels(sad)
    elif ball_position[0] == 7:
        sense.set_pixels(happy)


def move_up(event):
    global bat_y
    if event.action == "pressed" and bat_y > 1:
        bat_y -= 1


def move_down(event):
    global bat_y
    if event.action == "pressed" and bat_y < 6:
        bat_y += 1


# Main loop
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down


def data_received(data):
    print("recv - {}".format(data))
    global opp_bat_y
    opp_bat_y = int(data)


print("Connecting")
c = BluetoothClient("RPi4-8G", data_received)

print("Sending")
while c.connected:
    draw_bat()
    draw_ball()
    sleep(0.25)
    sense.clear(0, 0, 0)
    c.send(str(bat_y))


c.disconnect()