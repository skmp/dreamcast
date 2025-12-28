#!/usr/bin/env python3
import sys
import struct

WIDTH = 256
HEIGHT = 256
PIXELS = WIDTH * HEIGHT

def clamp(v, maxv):
    return max(0, min(v, maxv))

def process(in_path, out_path, gain=2.0):
    with open(in_path, "rb") as f:
        data = f.read()

    if len(data) != PIXELS * 2:
        raise ValueError(f"Expected {PIXELS*2} bytes, got {len(data)}")

    out = bytearray(len(data))

    for i in range(PIXELS):
        # RGB565 is little-endian in most raw dumps
        pixel = struct.unpack_from("<H", data, i * 2)[0]

        r = (pixel >> 11) & 0x1F
        g = (pixel >> 5) & 0x3F
        b = pixel & 0x1F

        r = clamp(int(r * gain), 31)
        g = clamp(int(g * gain), 63)
        b = clamp(int(b * gain), 31)

        new_pixel = (r << 11) | (g << 5) | b
        struct.pack_into("<H", out, i * 2, new_pixel)

    with open(out_path, "wb") as f:
        f.write(out)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: rgb565_brightness.py input.bin output.bin")
        sys.exit(1)

    process(sys.argv[1], sys.argv[2])
