from gpiozero import LED
from time import sleep

# tri-color LED is hooked to GPIO pins 17, 27 and 22.  These need to be statically allocated at this level
# rather than looking them up in a table due to the way GPIO allocates pins *once*.
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
        _red_led.on() if value == True else _red_led.off()
    elif color == "green":
        _green_led.on() if value == True else _green_led.off()
    elif color == "blue":
        _blue_led.on() if value == True else _blue_led.off()
    else:
        raise ValueError("Invalid color name" + color)

def led_red(value):
    _led_color("red", value)

def led_green(value):
    _led_color("green", value)

def led_blue(value):
    _led_color("blue", value)

def led_cyan(value):
    led_blue(value)
    led_green(value)

def led_yellow(value):
    led_red(value)
    led_green(value)

def led_violet(value):
    led_red(value)
    led_blue(value)

def led_all(value):
    led_red(value)
    led_blue(value)
    led_green(value)
        
def led_colors():
    l = []
    for fn in _led_functions():
        l.append(fn)
    return l

def led_color(color, value):
    _led_functions()[color](value)

def led_color_blink(col, count, interval):
    i = 0
    while i < count:
        led_color(col, True)
        sleep(0.2)
        led_color(col, False)
        sleep(interval)
        i = i + 1
