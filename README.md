# Engineering 3 Documentation 

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Ultrasonic Sensor](#Ultrasonic Sensor)
* [Motor_Control](#Motor_Control)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Ultrasonic Sensor

### Description & Code
For this assignment, we had to use an HC-SRO4 (ultrasonic sensor) to measure the distance to an object an then print out that value to the serial monitor. Then, we coded the neopixel to change color based on the distance; it should turn red when the object is less than 5cm aways, and green when its above 35 cm. In between, the color should be based on the gradient below:
![Gradient](./images/Gradient.png)
```python
Code goes here

```

### Evidence

### Wiring
![Ultrasonic Distance Sensor Wiring](./images/UltrasonicWiring.png)
### Reflection
The wiring for the ulrasonic distance sensor was easy; only four wires directly to the metro board were needed. However, running successfull code proved much more challenging. I had a multitude of issues trying to receive data from the ultrasonic sensor. We then learned that we had to change all the libraries to be compatible with the ultrasonic sensor, changing the version from CircuitPython 8 to 7. The second part that was challenging with code was making a working NeoPixel gradient that corresponded with the distance. 
I consulted the Internet to see the best way to map values in CircuitPython. I did not find any useful built-in functions, but I did find the stackoverflow link below: 
https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another 
The map code function looked complicated, so I wrote some examples to help me illustrate the underlying concepts better. Essentially, we shift the input range to start at 0, multiply the new x value by the ratio of the ranges, and then shift x to start at the true output range. Gudrun also helped me understand the intuition behind the gradient, spliting it up as a red-blue gradient from 5-20 cm and a blue-green gradient from 20-35cm. 

## Motor_Control

### Description & Code
For this assignment, we had to wire up a DC motor with a 6V battery pack, transistor, and diode. Then, we had to write CircuitPython code to make the motor speed up and slow down relative to the potentiometer value. 

Here is the code to control the motor based on potentiometer value:

```python
import board
from analogio import AnalogIn
import pwmio

potentiometer = AnalogIn(board.A5) # Init potentiometer 
motor_speed_control = pwmio.PWMOut(board.D13) # Set up PWM signal

while True:
    pot_position = potentiometer.value # Read current potentiometer value
    print((pot_position))
    motor_speed_control.duty_cycle = pot_position # Adjust motors speed
```
Controlling the speed of our DC motor w/ PWM involves suppling a series of high and low pulses to the motor. The key parameter, 'duty_cycle,' defines how much of one period the signal is "high" vs low. Higher duty cycle means faster-running motor. 

### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
![Motor Control Wiring Diagram](./images/MotorControlWiring.png)
Made in Fritzing

### Reflection
The most challenging part of the assignment by far was wiring. I learned that it's better to do the wiring modularly, instead of trying to wire everything at once; for instance, the potentiometer can be treated as a separate unit both code and wiring-wise. I did not realize the Mosfet Transistor's direction mattered - I was confused to why the motor was not running. Paul helped me debug my wiring, seeing that the Mosfet was flipped. This showed me that understanding what the parts of your system does is important, instead of blindly copying wiring diagrams from the internet. Additionally, I had many issues with controlling voltage. I had heard that the DC Motors could run with 9 Volts, and assumed that this fact held in this system. However, because we have a Mosfet transistor in the circuit, we should only use 6 Volts. The burning at the bottom of the Metro board signalled to me the severe voltage issue. In the future, I should try to thoroughly understand the mechanisms of new components so that I can properly debug and wire them up.











## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection

