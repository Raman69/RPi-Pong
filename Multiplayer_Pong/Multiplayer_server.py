from bluedot.btcomm import BluetoothServer
from time import sleep
from signal import pause
from sense_hat import SenseHat
import os

opp_bat_y = 4
bat_y = 4
sense = SenseHat()
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
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



def data_received(data):
    print("recv - {}".format(data))
    # if data == "1":
    #     sense.stick.wait_for_event()
    #     os.system('python /home/pi/RPi-Pong/Main_Interface.py')
    # elif data == "0":
    #     sense.stick.wait_for_event()
    #     os.system('python /home/pi/RPi-Pong/Main_Interface.py')
    global opp_bat_y
    opp_bat_y = int(data)
    if opp_bat_y > 6 :
        opp_bat_y = 6
    elif opp_bat_y < 1 :
        opp_bat_y = 1
    # server.send(data)


def client_connected():
    global server
    print(f"Connected to {server.client_address}")
    # Defining sense HAT and clearing LED matrix
    #sense = SenseHat()
    sense.clear()
    sense.lowlight = True

    global opp_bat_y
    global bat_y
    ball_position = [4, 4]
    ball_velocity = [1, 1]

    # Functions
    def draw_bat():
        global bat_y
        sense.set_pixel(7, bat_y + 1, white)
        sense.set_pixel(7, bat_y, white)
        sense.set_pixel(7, bat_y - 1, white)
        sense.set_pixel(0, opp_bat_y + 1, red)
        sense.set_pixel(0, opp_bat_y, red)
        sense.set_pixel(0, opp_bat_y - 1, red)

    def draw_ball():
        global opp_bat_y
        sense.set_pixel(ball_position[0], ball_position[1], blue)
        ball_position[0] += ball_velocity[0]
        if ball_position[0] == 0:
            ball_velocity[0] = -ball_velocity[0]
        ball_position[1] += ball_velocity[1]
        if ball_position[1] == 7 or ball_position[1] == 0:
            ball_velocity[1] = -ball_velocity[1]

        if ball_position[0] == 1 and (opp_bat_y - 2) <= ball_position[1] <= (
            opp_bat_y + 2
        ):
            ball_velocity[0] = -ball_velocity[0]
        if ball_position[0] == 6 and (bat_y - 2) <= ball_position[1] <= (bat_y + 2):
            ball_velocity[0] = -ball_velocity[0]

        if ball_position[0] == 0:
            sense.set_pixels(happy)
            server.send("101")
            sense.stick.wait_for_event()
            server.stop()
            os.system('python /home/pi/RPi-Pong/Main_Interface.py')
        elif ball_position[0] == 7:
            sense.set_pixels(sad)
            server.send("100")
            sense.stick.wait_for_event()
            server.stop()
            os.system('python /home/pi/RPi-Pong/Main_Interface.py')

    def move_up(event):
        global bat_y
        if event.action == "pressed" and bat_y > 1:
            bat_y -= 1

    def move_down(event):
        global bat_y
        if event.action == "pressed" and bat_y < 6:
            bat_y += 1

    def middle(event):
        if event.action == "hold":
            server.disconnect_client()
            server.stop()
            os.system('python /home/pi/RPi-Pong/Main_Interface.py')
    # Main loop
    sense.stick.direction_up = move_up
    sense.stick.direction_down = move_down
    sense.stick.direction_middle = middle

    while server.client_connected:
        draw_bat()
        draw_ball()
        sleep(0.25)
        sense.clear(0, 0, 0)
        server.send(str(bat_y))


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
    os.system('python /home/pi/RPi-Pong/Main_Interface.py')
except KeyboardInterrupt as e:
    print("cancelled by user")
finally:
    print("stopping")
    server.stop()
print("stopped")
