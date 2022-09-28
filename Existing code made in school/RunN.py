from readwrite import*
from LEDmatrix import*
from bouncer import*
from time import sleep
clear()
while True:
    r = open("led.txt")
    lines = r.readline()
    if lines == "1":
        revbounce()
        bounce()
        tw("0")
        clear()
