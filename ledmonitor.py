#!/bin/python3

"""
This is the primary script to run which basically loops forever and display
the network status based on pinging some known addresses on the tri-color
status LED wired to some GPIO pins.
"""

from time import sleep
from pythonping import ping
from ledcontrol import led_color, led_color_blink
from datetime import datetime
import sys
import os
import logging

addresses = {
    "8.8.8.8": 		"green",    # Google
    "10.11.100.248":	"yellow",   # Near radio P2P
    "10.11.100.249":	"yellow",   # Far radio P2P
    "10.11.111.250":	"cyan",     # Far switch
    "10.11.111.248":	"violet",   # Near ISP radio
    "10.11.111.249":	"violet",   # Far ISP radio
    "10.11.100.254":	"red",      # Great Firewall
}

logging.basicConfig(filename='/tmp/ledmonitor.log', level=logging.DEBUG)


def eep(msg, warn=True):
    """Scream about some important problem"""
    today = datetime.now()
    date_str = today.strftime("%Y/%m/%d %R")
    log_str = date_str + " " + msg
    if warn:
        logging.warning(log_str)
    else:
        logging.error(log_str)


while True:
    FAIL_CNT = 0
    for adr in addresses.items():
        col = addresses[adr]
        try:
            x = ping(adr, count=1, size=992)
            if x.success():
                led_color(col, True)
                sleep(5)
                break
            else:
                if ++FAIL_CNT > 3:
                    led_color("red", True)
                    eep("fail count > 3 for ip " + adr)
                    sleep(2)
                    fail = 0
                else:
                    # Let's have a blink spasm
                    led_color_blink(col, 5, 0.2)
                    eep("spazzing on ip " + adr + " with color " + col)

        except PermissionError:
            print("You have to run this as root")
            eep("Attempt to run agent as non-root id " + os.getuid())
            sys.exit(1)

        except BaseException:
            # Usually means the network has violently disconnected
            led_color_blink("red", 5, 0.2)
            eep("exception path triggered on " + adr, False)
