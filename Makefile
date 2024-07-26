.PHONY: help sync screen

help:
	@echo "Usage:"
	@echo "  rsync copy code to board:  make sync"
	@echo "  start terminal emulator:   make screen"

# This is for syncing current code to CIRCUITPY drive on macOS.
sync:
	xattr -cr code.py
	rsync -rcvO code.py /Volumes/CIRCUITPY/code.py
	sync

# Start serial terminal at fast baud rate with no flow control (-fn) using the
# serial device that happens to enumerate when I plug the board into my mac.
# It's very likely the device name may be different on other systems.
screen:
	screen -fn /dev/tty.usbmodem* 115200
