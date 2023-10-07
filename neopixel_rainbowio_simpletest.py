# SPDX-FileCopyrightText: 2022 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board 
import neopixel

NUMPIXELS = 12  # Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.2  #x A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.NEOPIXEL  # This is the default pin on the 5x5 NeoPixel Grid BFF.

pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)

def colorwheel(color_value):
    """
    A colorwheel. ``0`` and ``255`` are red, ``85`` is green, and ``170`` is blue, with the values
    between being the rest of the rainbow.

    :param int color_value: 0-255 of color value to return
    :return: tuple of RGB values
    """
    color_value = int(color_value)
    if color_value < 0 or color_value > 255:
        r = 0
        g = 0
        b = 0
    elif color_value < 85:
        r = int(255 - color_value * 3)
        g = int(color_value * 3)
        b = 0
    elif color_value < 170:
        color_value -= 85
        r = 0
        g = int(255 - color_value * 3)
        b = int(color_value * 3)
    else:
        color_value -= 170
        r = int(color_value * 3)
        g = 0
        b = int(255 - color_value * 3)
    return r << 16 | g << 8 | b

def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixels[pixel] = colorwheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    rainbow_cycle(SPEED)
    print("HI")
