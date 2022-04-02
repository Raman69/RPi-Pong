from LEDmatrix import *


num = 0
B = [0,0,255]
X = [0,0,0]
one = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    B,B,X,X,X,X,X,X,
    B,B,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]


two = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,B,B,X,X,X,X,
    X,X,B,B,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]


three = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,B,B,X,X,
    X,X,X,X,B,B,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]

four = [
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,B,B,
    X,X,X,X,X,X,B,B,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X,
    X,X,X,X,X,X,X,X
    ]


def bounce():
    display_pixels(one)
    delay(0.05)
    display_pixels(two)
    delay(0.05)
    display_pixels(three)
    delay(0.05)
    display_pixels(four)
    

def revbounce():
    display_pixels(four)
    delay(0.05)
    display_pixels(three)
    delay(0.05)
    display_pixels(two)
    delay(0.05)
    display_pixels(one)

while True:
    bounce()
