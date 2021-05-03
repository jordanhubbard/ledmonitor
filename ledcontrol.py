from gpiozero import LED
from time import sleep

# tri-color LED is hooked to GPIO pins 17, 27 and 22
_led_ports = {
    "red":	17,
    "green":	27,
    "blue":	22,
}

_led_functions = {
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

def _led_color(color, state):
    l = LED(_led_ports[color])
    l.on() if state == True else l.off()

def led_red(state):
    _led_color("red", state)

def led_green(state):
    _led_color("green", state)

def led_blue(state):
    _led_color("blue", state)

def led_cyan(state):
    led_blue(state)
    led_green(state)

def led_yellow(state):
    led_red(state)
    led_green(state)

def led_violet(state):
    led_red(state)
    led_blue(state)

def led_all(state):
    led_red(state)
    led_blue(state)
    led_green(state)
        
def led_colors():
    l = []
    for fn in _led_functions:
        l.append(fn)
    return l

def led_color(color, state):
    _led_functions[color](state)

def led_color_blink(col, count, interval):
    for r in range(count):
        led_color(col, True)
        sleep(interval)
        led_color(col, False)



    
