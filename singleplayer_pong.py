from select import select
from sense_hat import SenseHat
import os
import pygame
from pygame.locals import *
from time import sleep

# Defining sense HAT and clearing LED matrix
sense = SenseHat()
sense.clear()
sense.lowlight = True

white = (255, 255, 255)
blue = (0, 0, 255)
bat_y = 4
ball_position = [0, 0]
ball_velocity = [1, 1]
w = [255,255,255]
x = [0,0,0]
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

# Functions
def draw_bat():
    sense.set_pixel(7, bat_y + 1, white)
    sense.set_pixel(7, bat_y, white)
    sense.set_pixel(7, bat_y - 1, white)

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], blue)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] == 0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 6 and (bat_y-2) <= ball_position[1] <= (bat_y+2):
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[0] == 7:
        sense.set_pixels(sad)
        os._exit(0)

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
while True:
    draw_bat()
    draw_ball()
    sleep(0.25)
    sense.clear(0, 0, 0)
