#!/bin/env python3

# Mandelbrot Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop


# This color gradient contains 100 color steps.

MAX_ITERATIONS = len(gradient)
z = 0
pixel = complex(0, 0)  # z0


def paint(fractals, imagename):
    """Paint a Fractal image into the TKinter PhotoImage canvas.
    This code creates an image which is 512x512 pixels in size."""

    global gradient
    global img

    fractal = fractals[imagename]

    # Figure out how the boundaries of the PhotoImage relate to coordinates on
    # the imaginary plane.
    minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
    maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
    miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
    maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

    # Display the image on the screen
    canvas = Canvas(window, width=1024, height=1024, bg=gradient[0])
    canvas.pack()
    canvas.create_image((512, 512), image=img, state="normal")

    # At this scale, how much length and height on the imaginary plane does one
    # pixel take?
    pixelsize = abs(maxx - minx) / 1024

    portion = int(1024 / 64)
    total_pixels = 1048576
    for row in range(1024, 0, -1):
        for col in range(1024):
            x = minx + col * pixelsize
            y = miny + row * pixelsize
            color = colorOfThePixel(complex(x, y), gradient)
            img.put(color, (col, 1024 - row))
        window.update()  # display a row of pixels


def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")


# These are the different views of the Mandelbrot set you can make with this
# program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.
images = {
        'fullmandelbrot': {
            'centerX': -0.6,
            'centerY': 0.0,
            'axisLen': 2.5,
            },

        'spiral0': {
            'centerX': -0.761335372924805,
            'centerY': 0.0835704803466797,
            'axisLen': 0.004978179931102462,
            },

        'spiral1': {
            'centerX': -0.747,
            'centerY': 0.1075,
            'axisLen': 0.002,
            },

        'seahorse': {
            'centerX': -0.745,
            'centerY': 0.105,
            'axisLen': 0.01,
            },

        'elephants': {
            'centerX':  0.30820836067024604,
            'centerY':  0.030620936230004017,
            'axisLen':  0.03,
            },

        'leaf': {
            'centerX': -1.543577002,
            'centerY': -0.000058690069,
            'axisLen':  0.000051248888,
            },
        }


if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in images:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in images:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in images:
        print(f"\t{i}")
    sys.exit(1)

else:
    image = sys.argv[1]


# Set up the GUI so that we can paint the fractal image on the screen
window = Tk()
img = PhotoImage(width=1024, height=1024)
paint(images, image)

# Save the image as a PNG
img.write(f"{image}.png")
print(f"Wrote image {image}.png")

# Call tkinter.mainloop so the GUI remains open
mainloop()
