#!/bin/python3

from time import sleep
from ledcontrol import *

def test_leds(sleep_interval):
    colors = led_colors()
    while True:
        for col in colors:
            led_all(False)
            print(col + " LED is ON")
            led_color(col, True)
            sleep(sleep_interval)

print("Blinking red LED 5 times")
led_color_blink("red", 5, 0.2)
test_leds(0.5)
