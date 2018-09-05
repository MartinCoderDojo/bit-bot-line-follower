from microbit import *

leftLine = pin11
rightLine = pin5

# pin 0 = left speed
# pin 8 = left direction
# pin 1 = right speed
# pin 12 = right direction
# Direction = 0 for forward, 1 for backward


def moveRobot(pin0Val, pin8Val, pin1Val, pin12Val):
    pin0.write_digital(pin0Val)
    pin8.write_digital(pin8Val)
    pin1.write_digital(pin1Val)
    pin12.write_digital(pin12Val)


def forward():
    moveRobot(1, 0, 1, 0)


def turnRight():
    moveRobot(1, 0, 0, 0)


def turnLeft():
    moveRobot(0, 0, 1, 0)


def stop():
    moveRobot(0, 0, 0, 0)


def reverse():
    moveRobot(1, 1, 1, 1)


while True:
    lline = leftLine.read_digital()
    rline = rightLine.read_digital()

    if ((lline == 1) and (rline == 0)):
        turnLeft()
    elif ((lline == 0) and (rline == 1)):
        turnRight()
    elif ((lline == 1) and (rline == 1)):
        forward()
    else:
        stop()
