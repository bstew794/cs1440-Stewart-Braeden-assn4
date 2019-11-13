#!/bin/env python3

# Mandelbrot Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop

# These are the different views of the Mandelbrot set you can make with this
# program.
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'image'.


def pixelsWrittenSoFar(rows, cols):
    pixels = rows * cols
    print(f"{pixels} pixels have been output so far")


def getMandelIndex(pixel, constant, gradient):
    """Return the index of the color of the current pixel within the Julia set
    in the gradient array"""

    gradLength = len(gradient)

    # Here gradLength refers to the number of colors in the gradient
    for i in range(gradLength):
        pixel = pixel * pixel + constant  # Iteratively compute z1, z2, z3 ...
        if abs(pixel) > 2:
            return i

    return gradLength - 1


if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in fractals:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in fractals:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in fractals:
        print(f"\t{i}")
    sys.exit(1)

else:
    image = sys.argv[1]

# Save the image as a PNG
img.write(f"{image}.png")
print(f"Wrote image {image}.png")

# Call tkinter.mainloop so the GUI remains open
mainloop()
