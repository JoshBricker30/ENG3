import time
import board
import pwmio
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull


# Create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
servo1 = servo.Servo(pwm)

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

# Initialize Button2
button2 = DigitalInOut(board.D5) 
button2.direction = Direction.INPUT
button2.pull = Pull.DOWN

current_angle = 0  # Initialize the angle

while True:
    if button.value:  # Button1 is pressed, turn clockwise
        print("Button 1 is pressed \t")
        print(current_angle)
        current_angle = current_angle + 10 
        current_angle = max(0, min(180, current_angle)) # Range restrict because 180 servo
        servo1.angle = current_angle # Set new angle
    time.sleep(0.01)  

    if button2.value:  # Button2 is pressed, turn counterclockwise
        print("Button 2 is pressed \t")
        print(current_angle)
        current_angle = current_angle - 10
        current_angle = max(0, min(180, current_angle))
        servo1.angle = current_angle  
    time.sleep(0.01)  