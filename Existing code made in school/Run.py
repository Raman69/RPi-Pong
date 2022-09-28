from readwrite import*
from LEDmatrix import*
from bouncer import*
from time import sleep
clear()
while True:
    r = open("led.txt")
    lines = r.readline()
    
    if lines == "0":
        revbounce()
        bounce()
        tw("1")
        clear()
   
    

        
        
        



