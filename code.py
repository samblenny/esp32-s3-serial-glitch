# Expected behavior:
#   At 1 second intervals, Neopixel toggles and timestamp prints. This should
#   keep happening indefinitely.
#
# Actual behavior:
#   Prior to locking the screen (macOS Sonoma 14.5 + M1 Mac mini), Neopixel
#   toggles and timestamps print as expected. After locking the screen for
#   about 5 minutes, then logging back in, the Neopixel still blinks but the
#   timestamps do not print to the serial console.
#
from time import monotonic, sleep
from board import NEOPIXEL, NEOPIXEL_POWER
from neopixel_write import neopixel_write
from digitalio import DigitalInOut, Direction


np = DigitalInOut(NEOPIXEL)
pwr = DigitalInOut(NEOPIXEL_POWER)
np.direction = Direction.OUTPUT
pwr.direction = Direction.OUTPUT
pwr.value = True
epoch = monotonic()
colors = [bytearray([0, 0, 0]), bytearray([5, 0, 5])]
i = 0
while True:
    neopixel_write(np, colors[i])
    print(monotonic() - epoch)
    i ^= 1
    sleep(1)
