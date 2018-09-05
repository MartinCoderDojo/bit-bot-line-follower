from microbit import *
import neopixel

leftLine = pin11
rightLine = pin5

np = neopixel.NeoPixel(pin13, 12)

# pin 0 = left speed
# pin 8 = left direction
# pin 1 = right speed
# pin 12 = right direction
# Direction = 0 for forward, 1 for backward


def moveRobot(pin0Val, pin8Val, pin1Val, pin12Val):
    pin0.write_analog(pin0Val)
    pin8.write_digital(pin8Val)
    pin1.write_analog(pin1Val)
    pin12.write_digital(pin12Val)
    sleep(100)


def convert(speed):
    if speed > 0:
        return (speed * 1023) / 100.0
    return 1023 - ((abs(speed) * 1023) / 100.0)


def forward(speed):
    moveRobot(convert(speed), 0, convert(speed), 0)


def turnRight(speed):
    moveRobot(convert(speed), 0, 0, 0)


def turnLeft(speed):
    moveRobot(0, 0, convert(speed), 0)


def stop():
    moveRobot(0, 0, 0, 0)


def reverse(speed):
    moveRobot(convert(-speed), 1, convert(-speed), 1)


def turn_on_neopixel(neopixel, red, green, blue):
    np[neopixel] = (red, green, blue)


def turn_on_left_neopixels(red, green, blue):
    for i in range(6):
        np[i] = (red, green, blue)


def turn_on_right_neopixels(red, green, blue):
    for i in range(6, 12):
        np[i] = (red, green, blue)


def turn_on_all_neopixels(red, green, blue):
    for i in range(12):
        np[i] = (red, green, blue)


def sound_horn():
    pin14.write_digital(1)
    sleep(400)
    pin14.write_digital(0)

# Left sensor and right sensor both 1: on black line
# Left sensor 1 and right sensor 0: left sensor is on the line
# Left sensor 0 and right sensor 1: right sensor is on the line
# Left sensor and right sensor both 0: lost the line


while True:
    lline = leftLine.read_digital()
    rline = rightLine.read_digital()

    if ((lline == 1) and (rline == 1)):
        forward(100)
    elif ((lline == 1) and (rline == 0)):
        ???
    elif ???:
        ???
    else:
        ???
