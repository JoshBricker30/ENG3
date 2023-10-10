import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D6) # Init ultrasonic sensor

# Set up NeoPixel
NUMPIXELS = 1  
BRIGHTNESS = 0.2  
PIN = board.NEOPIXEL  
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

# Mapping function to convert x from input range to corresponding value in output range
# x: value wanted to map | in_min & in_max: input range of x | out_min & out_max: output range
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

while True:
    try:
        cm = sonar.distance # receive ultrasonic distance
        print(cm)                 
        if(cm < 5): # Below 5, keep red
            pixels.fill((255, 0, 0))
        elif(cm < 20): # Blend between red and blue
            ratio = map_value(cm, 5, 20, 0, 1) #ratio of r:b
            r = int(255 * (1 - ratio))
            b = int(255 * ratio)
            pixels.fill((r, 0, b))
        elif(cm < 35): # Blend between blue and green 
            ratio = map_value(cm, 20, 35, 0, 1) #ratio of b:g
            b = int(255 * (1 - ratio))
            g = int(255 * ratio)
            pixels.fill((0, g, b))
        else: # Above 35, keep green
            pixels.fill((0, 255, 0))
        pixels.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)