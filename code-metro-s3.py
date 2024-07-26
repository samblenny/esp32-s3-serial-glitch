from board import D9, D10, SPI
from digitalio import DigitalInOut, Direction
from displayio import release_displays
from fourwire import FourWire
from time import monotonic, sleep
from adafruit_ili9341 import ILI9341

release_displays()
bus = FourWire(SPI(), command=D9, chip_select=D10)
display = ILI9341(bus, width=320, height=240)
display.rotation = 180  # landscape with Metro S3 USB port on the right
epoch = monotonic()
while True:
    print(monotonic() - epoch)
    sleep(1)
