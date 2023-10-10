import board
from analogio import AnalogIn
import pwmio

potentiometer = AnalogIn(board.A5) #init potentiometer 
motor_speed_control = pwmio.PWMOut(board.D13) #set up PWM signal

while True:
    pot_position = potentiometer.value # Read current potentiometer value
    print((pot_position))
    motor_speed_control.duty_cycle = pot_position # Adjust motors speed