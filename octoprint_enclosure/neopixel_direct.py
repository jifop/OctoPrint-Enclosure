"""
Modified by Tim Shotter 02/01/23

install required libs before running:
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka

"""

import board
import neopixel
import sys
import time

LED_INVERT = False
LED_FREQ_HZ = 800000

if len(sys.argv) == 8:
    LED_PIN = int(sys.argv[1])
    LED_COUNT = int(sys.argv[2])
    LED_BRIGHTNESS = int(sys.argv[3])
    red = int(sys.argv[4])
    green = int(sys.argv[5])
    blue = int(sys.argv[6])
    LED_DMA = int(sys.argv[7])
else:
    print("fail")
    sys.exit(1)

pixels = neopixel.NeoPixel(board.LED_PIN, LED_COUNT)
pixels.fill((red, green, blue))

print("ok")
