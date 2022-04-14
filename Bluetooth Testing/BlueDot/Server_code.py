from bluedot.btcomm import BluetoothServer
from time import sleep
from signal import pause

number = 100

def data_received(data):
    print("recv - {}".format(data))
    #server.send(data)


def client_connected():
    global number
    print(f"Connected to {server.client_address}")
    while server.client_connected:
        server.send(str(number))
        number-=1
        sleep(1)


def client_disconnected():
    print("client disconnected")


print("init")
server = BluetoothServer(
    data_received,
    auto_start=False,
    when_client_connects=client_connected,
    when_client_disconnects=client_disconnected,
)

print("starting")
server.start()
print(server.server_address)
print("waiting for connection")

try:
    pause()
except KeyboardInterrupt as e:
    print("cancelled by user")
finally:
    print("stopping")
    server.stop()
print("stopped")
