from gpiozero import LED
from time import sleep

# tri-color LED is hooked to GPIO pins 17, 27 and 22
_led_ports = dict([
    ("red", 17),
    ("green", 27),
    ("blue", 22)])

# Obviously, with RGB LED any color combination is possible with color blending
# but I don't feel like doing that and I already have more primary/secondary colors
# than I need!
def led_red(state):
    if state == True:
        LED(_led_ports["red"]).on()
    else:
        LED(_led_ports["red"]).off()

def led_green(state):
    if state == True:
        LED(_led_ports["green"]).on()
    else:
        LED(_led_ports["green"]).off()

def led_blue(state):
    if state == True:
        LED(_led_ports["blue"]).on()
    else:
        LED(_led_ports["blue"]).off()

def led_cyan(state):
    blue_led(state)
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
        
def led_functions():
    return dict([
        ("black",	led_all,	True),
        ("red",		led_red,	True),
        ("green",	led_green,	True),
        ("blue",	led_blue,	True),
        ("cyan",	led_cyan,	True),
        ("yellow",	led_yellow,	True),
        ("violet",	led_violet,	True),
        ("white",	led_all,	False)])

def led_colors():
    fns = led_functions
    l = []
    for fn in fns:
        l.append(fn)
    return l

def led_color(color, state):
    led_functions()[color][1](state)

def led_color_blink(col, count, interval):
    for r in range(count):
        led_color(col, True)
        sleep(interval)
        led_color(col, False)



    
