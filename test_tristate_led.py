#!/bin/python3

from time import sleep
from ledcontrol import led_colors, led_color, led_color_blink


def test_leds(sleep_interval):
    colors = led_colors()
    while True:
        for col in colors:
            print(col + " LED is ON")
            led_color(col, True)
            sleep(sleep_interval)
            led_color(col, False)
            print(col + " is blinking")
            led_color_blink(col, 5, 0.2)


test_leds(2)
