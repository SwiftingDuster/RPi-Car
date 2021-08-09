#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import HiwonderSDK.Board as Board
import argparse
import time

# Define functions which animate LEDs in various ways.
def colorWipe(color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(Board.RGB.numPixels()):
        Board.RGB.setPixelColor(i, color)
        Board.RGB.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, Board.RGB.numPixels(), 3):
                Board.RGB.setPixelColor(i + q, color)
            Board.RGB.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, Board.RGB.numPixels(), 3):
                Board.RGB.setPixelColor(i + q, 0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Board.PixelColor(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Board.PixelColor(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Board.PixelColor(0, pos * 3, 255 - pos * 3)


def rainbow(wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(Board.RGB.numPixels()):
            Board.RGB.setPixelColor(i, wheel((i + j) & 255))
        Board.RGB.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(Board.RGB.numPixels()):
            Board.RGB.setPixelColor(i, wheel(
                (int(i * 256 / Board.RGB.numPixels()) + j) & 255))
        Board.RGB.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, Board.RGB.numPixels(), 3):
                Board.RGB.setPixelColor(i + q, wheel((i + j) % 255))
            Board.RGB.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, Board.RGB.numPixels(), 3):
                Board.RGB.setPixelColor(i + q, 0)


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')
    try:

        while True:
            print('Color wipe animations.')
            colorWipe(Board.PixelColor(255, 0, 0))  # Red wipe
            time.sleep(1)
            colorWipe(Board.PixelColor(0, 255, 0))  # Blue wipe
            time.sleep(1)
            colorWipe(Board.PixelColor(0, 0, 255))  # Green wipe
            time.sleep(1)
            print('Theater chase animations.')
            theaterChase(Board.PixelColor(127, 127, 127))  # White theater chase
            time.sleep(1)
            theaterChase(Board.PixelColor(127, 0, 0))  # Red theater chase
            time.sleep(1)
            theaterChase(Board.PixelColor(0, 0, 127))  # Blue theater chase
            time.sleep(1)
            print('Rainbow animations.')
            rainbow()
            time.sleep(1)
            rainbowCycle()
            time.sleep(1)
            theaterChaseRainbow()

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(Color(0, 0, 0), 10)
