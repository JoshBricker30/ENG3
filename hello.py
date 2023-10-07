import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

servo1 = servo.Servo(pwm) # Servo Object

# Button 1: Clockwise
button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

# Button 2: Counterclockwise
button2 = DigitalInOut(board.D5)
button2.direction = Direction.INPUT
button2.pull = Pull.DOWN


current_angle = 0  # Initialize the angle

while True:
    print(button.value)
    if button.value:  # Button is pressed (remember, we're assuming it's pull-down)
        print("btn1 pressed \t")
        print(current_angle)
        current_angle = current_angle + 10
        current_angle = max(0, min(360, current_angle))
        servo1.angle = current_angle  # Set the new angle
    time.sleep(0.05)  # Small delay to avoid excessive checking

    print(button2.value)
    if button2.value:  # Button is pressed (remember, we're assuming it's pull-down)
        print("btn2 pressed \t")
        print(current_angle)
        current_angle = current_angle - 10
        current_angle = max(0, min(360, current_angle))
        servo1.angle = current_angle  # Set the new angle
    time.sleep(0.05)  # Small delay to avoid excessive checking