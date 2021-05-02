from time import sleep
from ledcontrol import *

def test_leds(sleep_interval):
    colors = led_colors()
    while True:
        for col in colors:
            leds_all_off()
            print(col + " LED is ON")
            led_color_on(col)
            sleep(sleep_interval)

led_color_blink("red", 5, 0.2)
test_leds(0.5)


    
