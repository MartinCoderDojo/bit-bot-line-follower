from microbit import *


def moveRobot(pin0Val, pin8Val, pin1Val, pin12Val):
    pin0.write_analog(pin0Val)
    pin8.write_digital(pin8Val)
    pin1.write_analog(pin1Val)
    pin12.write_digital(pin12Val)


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


forward(100)
sleep(1000)
stop()
