from time import sleep
from gpiozero import LED

# tri-color LED is hooked to GPIO pins 17, 27 and 22.  These need to be
# statically allocated at this level rather than looking them up in a table
# due to the way GPIO allocates pins *once*.
_red_led = LED(17)
_green_led = LED(27)
_blue_led = LED(22)


def _led_functions():
    return {
      "red":	led_red,
      "green":	led_green,
      "blue":	led_blue,
      "cyan":	led_cyan,
      "yellow":	led_yellow,
      "violet":	led_violet,
      "white":	led_all,
    }


# Obviously, with RGB LED any color combination is possible with color blending
# but I don't feel like doing that and I already have more primary/secondary
# colors than I need!
def _led_color(color, value):
    if color == "red":
        if value:
            _red_led.on()
        else:
            _red_led.off()
    elif color == "green":
        if value:
            _green_led.on()
        else:
            _green_led.off()
    elif color == "blue":
        if value:
            _blue_led.on()
        else:
            _blue_led.off()
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
    """Power on/off LED color of cyan, using a combination of blue and green"""
    led_blue(value)
    led_green(value)


def led_yellow(value):
    """Power on/off LED color of yellow, using a combination of red and green"""
    led_red(value)
    led_green(value)


def led_violet(value):
    """Power on/off LED color of violet, using a combination of red and blue"""
    led_red(value)
    led_blue(value)


def led_all(value):
    """Power on/off all LEDs (white or black)"""
    led_red(value)
    led_blue(value)
    led_green(value)


def led_colors():
    """Return a list of all possible LED colors"""
    lst = []
    for fn in _led_functions():
        lst.append(fn)
    return lst


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
