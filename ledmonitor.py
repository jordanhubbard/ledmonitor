#!/bin/python3

"""
This is the primary script to run which basically loops forever and display
the network status based on pinging some known addresses on the tri-color
status LED wired to some GPIO pins.
"""

import sys
import os
import logging
import threading
from time import sleep
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pythonping import ping
from ledcontrol import led_color, led_color_blink

HOST_NAME = "netled.local"
SERVER_PORT = 8080
paging_hacker = False

WEB_CODE = """
<!DOCTYPE html>
<html>
<head>

<style>
.button {
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.button1 {
  background-color: white;
  color: black;
  border: 2px solid #4CAF50;
}

.button1:hover {
  background-color: #4CAF50;
  color: white;
}
</style>

<title>Press Button To Page Hacker</title>
</head>
<body>
<h1><p>Press the Button Below to Light Jordan's Light!</p></h1>
<form action="/page" method="get">
  <button class="button button1" type="submit" formaction="/page">PAGE PACKER</button>
</form>

</body>
</html>
"""

WEB_CODEPAGED = """
<!DOCTYPE html>
<html>
<head>
<title>PAGING</title>
</head>
<body>

<style>
.button {
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.button1 {
  background-color: white;
  color: black;
  border: 2px solid #FFAF50;
}

.button1:hover {
  background-color: #FFAF50;
  color: white;
}
</style>

<h2><p>You have paged the hacker! He will check his texts.</p></h2>
<form action="/" method="get">
  <button class="button button1" type="submit" formaction="/">RETURN TO PAGER</button>
</form>
</body>
</html>
"""

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
    """Simple embedded python web server"""
    def do_GET(self):
        """This is the default method which gets called on GET"""
        global paging_hacker
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(WEB_CODE, "utf-8"))
        elif self.path == "/page?":
            paging_hacker = True
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(WEB_CODEPAGED, "utf-8"))

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
    webServer = ThreadingHTTPServer((HOST_NAME, SERVER_PORT), MyServer)
    th = threading.Thread(target=webServer.serve_forever)
    eep("Server started http://%s:%s" % (HOST_NAME, SERVER_PORT))
    th.start()

while True:
    FAIL_CNT = 0
    if paging_hacker:
        led_color_blink("white", 10, 0.1)
        sleep(2)
        led_color_blink("white", 10, 0.1)
        sleep(2)
        led_color_blink("white", 10, 0.1)
        paging_hacker = False

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
