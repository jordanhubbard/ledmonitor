#!/bin/python3

"""
This is the primary script to run which basically loops forever and display
the network status based on pinging some known addresses on the tri-color
status LED wired to some GPIO pins.
"""

import sys
import os
import logging
from time import sleep
from datetime import datetime
from pythonping import ping
from ledcontrol import led_color, led_color_blink
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

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


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        led_color_blink("orange", 10, 0.1)

def eep(msg, warn=True):
    """Scream about some important problem"""
    today = datetime.now()
    date_str = today.strftime("%Y/%m/%d %R")
    log_str = date_str + " " + msg
    if warn:
        logging.warning(log_str)
    else:
        logging.error(log_str)

if __name__ == "__main__":        
    webServer = ThreadingHTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

while True:
    FAIL_CNT = 0
    for adr in addresses.items():
        ip = adr[0]
        col = adr[1]
        try:
            x = ping(ip, count=1, size=992)
            if x.success():
                led_color(col, True)
                sleep(5)
                break

            FAIL_CNT = FAIL_CNT + 1
            if FAIL_CNT > 3:
                led_color("red", True)
                eep("fail count > 3 for ip " + ip)
                sleep(2)
                FAIL_CNT = 0
            else:
                # Let's have a blink spasm
                led_color_blink(col, 5, 0.2)
                eep("spazzing on ip " + ip + " with color " + col)

        except PermissionError:
            print("You have to run this as root")
            eep("Attempt to run agent as non-root id " + os.getuid())
            sys.exit(1)

        except OSError:
            # Usually means the network has violently disconnected
            led_color_blink("red", 5, 0.2)
            eep("exception path triggered on " + ip, False)
