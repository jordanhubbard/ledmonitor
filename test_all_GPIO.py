#!/bin/python3

"""Simple test driver to see that all GPIO ports are working"""

from time import sleep
from gpiozero import LED

MAX_LED = 27
COMMON_ANODE = True

def test_pins(sleep_interval):
    """Run through all GPIO pins and turn each on and off"""
    i = 0
    while True:
        l = LED(i)
        print(str(i) + " on")
        if COMMON_ANODE == True:
            l.off()
        else:
            l.on()
        sleep(sleep_interval)
        print(str(i) + " off")
        if COMMON_ANODE == True:
            l.on()
        else:
            l.off()
        i = i + 1
        if i > MAX_LED:
            i = 0

test_pins(0.5)
