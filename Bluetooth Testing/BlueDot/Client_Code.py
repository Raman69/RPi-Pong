from bluedot.btcomm import BluetoothClient
from time import sleep
from signal import pause

number = 0

def data_received(data):
    print("recv - {}".format(data))


print("Connecting")
c = BluetoothClient("RPi4-8G", data_received)
print(f"Connected to {c.server}")

print("Sending")
while c.connected:
    c.send(str(number))
    number+=1
    sleep(1)

print("Disconnected from server")

try:
    pause()
except KeyboardInterrupt as e:
    print("cancelled by user")
finally:
    print("stopping")
    c.disconnect
print("stopped")
