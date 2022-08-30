"""All LED control functions are in this module"""

from time import sleep
from gpiozero import LED

# tri-color LED is hooked to GPIO pins 9, 10 and 11.  These need to be
# statically allocated at this level rather than looking them up in a table
# due to the way GPIO allocates pins *once*.
BLUE_LED = LED(11)
RED_LED = LED(10)
GREEN_LED = LED(9)

# If common anode LED, then True else set to False
COMMON_ANODE = True

def _led_functions():
    return {
        "red":		led_red,
        "green":	led_green,
        "blue":		led_blue,
        "cyan":		led_cyan,
        "yellow":	led_yellow,
        "violet":	led_violet,
        "white":	led_all,
    }


# Obviously, with RGB LED any color combination is possible with color blending
# but I don't feel like doing that and I already have more primary/secondary
# colors than I need!
def _led_color(color, value):
    if COMMON_ANODE == True:
        value = not value
    if color == "red":
        if value:
            RED_LED.on()
        else:
            RED_LED.off()
    elif color == "green":
        if value:
            GREEN_LED.on()
        else:
            GREEN_LED.off()
    elif color == "blue":
        if value:
            BLUE_LED.on()
        else:
            BLUE_LED.off()
    else:
        raise ValueError("Invalid color name" + color)


def led_red(value):
    """Power on/off the red LED based on value"""
    _led_color("red", value)


def led_green(value):
    """Power on/off the green LED based on value"""
    _led_color("green", value)


def led_blue(value):
    """Power on/off the blue LED based on value"""
    _led_color("blue", value)


def led_cyan(value):
    """Power on/off LED color cyan, using a combination of blue and green"""
    led_blue(value)
    led_green(value)


def led_yellow(value):
    """Power on/off LED color yellow, using a combination of red and green"""
    led_red(value)
    led_green(value)


def led_violet(value):
    """Power on/off LED color violet, using a combination of red and blue"""
    led_red(value)
    led_blue(value)


def led_all(value):
    """Power on/off all LEDs (white or black)"""
    led_red(value)
    led_blue(value)
    led_green(value)


def led_colors():
    """Return a list of all possible LED colors"""
    ret_list = []
    for func_iter in _led_functions():
        ret_list.append(func_iter)
    return ret_list


def led_color(color, value):
    """Convenience function to set any color value on or off"""
    _led_functions()[color](value)


def led_color_blink(col, count, interval):
    """Blink a specific color count times using a delay interval"""
    i = 0
    while i < count:
        led_color(col, True)
        sleep(0.2)
        led_color(col, False)
        sleep(interval)
        i = i + 1
