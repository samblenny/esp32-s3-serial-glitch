.PHONY: help bundle sync sync_s3 tty clean

help:
	@echo "Usage:"
	@echo "  rsync copy code to board:  make sync"
	@echo "  start terminal emulator:   make screen"

bundle:
	@mkdir -p build
	python3 bundle_builder.py

# This is for syncing current code to CIRCUITPY drive on macOS.
sync:
	xattr -cr code.py
	rsync -rcvO code.py /Volumes/CIRCUITPY/code.py
	sync

# This is for syncing current code to CIRCUITPY drive on macOS.
sync_s3: bundle
	xattr -cr code-metro-s3.py
	rsync -rcvO code-metro-s3.py /Volumes/CIRCUITPY/code.py
	sync

# Start serial terminal at fast baud rate with no flow control (-fn) using the
# serial device that happens to enumerate when I plug the board into my mac.
# It's very likely the device name may be different on other systems.
tty:
	screen -fn /dev/tty.usbmodem* 115200

clean:
	rm -rf build
