#!/usr/bin/env python3
from PIL import Image, ImageDraw

XMIN, XMAX = -2, 1
YMIN, YMAX = -1.2, 1.2
WIDTH = 2400
HEIGHT = int(WIDTH*(YMAX-YMIN)/(XMAX-XMIN))
MAX_ITER = 256;

img = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(img)

def mandelbrot(c):
    i = 0
    z = complex(0, 0)
    while i < MAX_ITER and abs(z) < 2:
        z = z*z + c
        i = i + 1
    return i

for x in range(0,WIDTH):
    for y in range(0, HEIGHT):
        m = mandelbrot(complex((x/WIDTH)*(XMAX-XMIN) + XMIN,
                               (y/HEIGHT)*(YMAX-YMIN) + YMIN))
        hue = int(255 * m / MAX_ITER) # Color depends on the # of iterations
        saturation = 255
        value = 255 if m < MAX_ITER else 0
        draw.point([x, y], (hue, saturation, value))

img.convert('RGB').save('mandelbrot.png', 'PNG')
