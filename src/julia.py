#!/bin/env python3

# Julia Set Visualizer

import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop

# This dictionary contains the different views of the Julia set you can make
# with this program.
#
# For convenience I have placed these into a dictionary so you may easily
# switch between them by entering the name of the image you want to generate
# into the variable 'i'.


def getJuliaColorIndex(pixel, constant, gradient):
    """Return the index of the color of the current pixel within the Julia set
    in the gradient array"""

    gradLength = len(gradient)

    # Here gradLength refers to the number of colors in the gradient
    for i in range(gradLength):
        pixel = pixel * pixel + constant  # Iteratively compute z1, z2, z3 ...
        if abs(pixel) > 2:
            return i

    return gradLength - 1

# Process command-line arguments, allowing the user to select their fractal


if len(sys.argv) < 2:
    print("Please provide the name of a fractal as an argument")
    for i in f:
        print(f"\t{i}")
    sys.exit(1)

elif sys.argv[1] not in f:
    print(f"ERROR: {sys.argv[1]} is not a valid fractal")
    print("Please choose one of the following:")
    for i in f:
        print(f"\t{i}")
    sys.exit(1)

else:
    i = sys.argv[1]

