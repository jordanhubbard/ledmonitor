from gpiozero import LED
from time import sleep

# tri-color LED is hooked to GPIO pins 17, 27 and 22
red_led = LED(17)
green_led = LED(27)
blue_led = LED(22)

# Obviously, with RGB LED any color combination is possible with color blending
# but I don't feel like doing that and I already have more primary/secondary colors
# than I need!
def led_colors():
    return ["red", "green", "blue", "yellow", "cyan", "violet", "white"]

def leds_all_off():
    red_led.off()
    green_led.off()
    blue_led.off()

def led_color_blink(col, count, interval):
    for r in range(count):
        led_color_on(col)
        sleep(interval)
        led_color_on("black")
        
def led_color_on(color):
    if color == "black":
        leds_all_off()
    elif color == "red":
        red_led.on()
    elif color == "green":
        green_led.on()
    elif color == "blue":
        blue_led.on()
    elif color == "cyan":
        blue_led.on()
        green_led.on()
    elif color == "yellow":
        red_led.on()
        green_led.on()
    elif color == "violet":
        red_led.on()
        blue_led.on()
    elif color == "white":
        red_led.on()
        blue_led.on()
        green_led.on()
    else:
        print("Invalid color selected: " + color)        



    
