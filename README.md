# ESP32-S3 Serial Glitch Reproducer

The USB serial output of my QT Py ESP32-S3 often becomes
unresponsive when I leave it plugged into an M1 Mac mini with macOS Sonoma
14.5. This happens both with CircuitPython 9.1.0 and 9.1.1.

Everything is normally fine with the screen unlocked. But, if I lock the
screen, then come back a bit later (5 minutes is usually enough), I will often
have to reset the board before I can see serial output again (reset button or
unplug/replug both work).

The weird thing is that when the USB serial output glitch is happening, my
CIRCUITPY drive is still available, my code still runs (LED blinks), and USB
serial input (from mac to the ESP32-S3) appears to still work. I say that
because, if I do a `screen -fn /dev/tty.usbmodem...`, then type Ctrl-C, it
causes the S3's LED to do an intermittent double-red blink in the same manner
as Ctrl-C under normal circumstances. But, when I do the Ctrl-C, none of the
usual output text appears in screen's terminal window. If I reset or eject the
CIRCUITPY drive, unplug the board, then plug it back in, the serial output
resumes working normally.

In macOS System Settings > Energy Saver, my settings are:
- Prevent automatic sleeping when the display is off: **OFF**
- Put hard disks to sleep when possible: **ON**
- Wake for network access: **OFF**
- Start up automatically after a power failure: **OFF**

In System Settings > Lock Screen, my settings are:
- Start Screen Saver when Inactive: **Never**
- Turn display off when inactive: **For 20 Minutes**
- Require password after screen saver begins or display is turned off:
  **After 5 seconds**


## Hardware

- Adafruit QT Py ESP32-S3 with 8MB Flash and no PSRAM
  ([product page](https://www.adafruit.com/product/5426),
  [learn guide](https://learn.adafruit.com/adafruit-qt-py-esp32-s3))
