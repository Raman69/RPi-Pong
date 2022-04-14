from tokenize import Number
from bluedot.btcomm import BluetoothClient
from datetime import datetime
from time import sleep
from signal import pause

won = False
number = 0

def data_received(data):
    print("recv - {}".format(data))


print("Connecting")
c = BluetoothClient("RPi4-8G", data_received)

print("Sending")
while True:
    c.send(str(number+1))
    sleep(1)
    if won == True:
        break

c.disconnect()
