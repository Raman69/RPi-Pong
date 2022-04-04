from select import select
from sense_hat import SenseHat
import os
import pygame
from pygame.locals import *
from time import sleep

# Defining LED matrix and clearing sense HAT
matrix = SenseHat()
matrix.clear()
matrix.lowlight = True

white = (255, 255, 255)
bat_y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

# Functions
def draw_bat():
    matrix.set_pixel(0, bat_y + 1, white)
    matrix.set_pixel(0, bat_y, white)
    matrix.set_pixel(0, bat_y - 1, white)


def move_up(event):
    global bat_y
    if event.action == "pressed" and bat_y > 1:
        bat_y -= 1


def move_down(event):
    global bat_y
    if event.action == "pressed" and bat_y < 6:
        bat_y += 1

# Main loop
matrix.stick.direction_up = move_up
matrix.stick.direction_down = move_down
while True:
    draw_bat()
    sleep(0.25)
    matrix.clear(0, 0, 0)

def tw(n):
    r = open("ball.txt")
    lines = r.readlines()
    w = open('ball.txt','w')
    write = w.writelines(n)
    a = open('ball.txt','a')
    a = a.writelines(n)
    r = open("ball.txt")
    lines = r.readline()

while True:
    for i in range(0,7):
        if ball_position < [7,i]:
            print("Ball next")
            tw(0)












