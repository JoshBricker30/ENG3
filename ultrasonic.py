import time
import board
import adafruit_hcsr04
from rainbowio import colorwheel
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D7, echo_pin=board.D6)

NUMPIXELS = 1  # Update this to match the number of LEDs.
BRIGHTNESS = 0.2  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

while True:
    try:
        cm = sonar.distance
        print(cm)                 
        if(cm < 5):
            pixels.fill((255, 0, 0))
        elif(cm > 35):   
            pixels.fill((0, 255, 0))
        else:
            pixels.fill((0, 0, 255))
        pixels.show()
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)